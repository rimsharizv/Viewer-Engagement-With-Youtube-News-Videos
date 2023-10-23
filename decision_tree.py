import sklearn
from sklearn import tree
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def analyze():
    df = pd.read_json('top_news.json', lines=True)

    # Create the statistics dataframe from the original dataframe
    sts = pd.DataFrame(columns = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount'])
    for stats in df['statistics']:
        if 'commentCount' in stats and 'viewCount' in stats and 'favoriteCount' in stats and 'dislikeCount' in stats and 'likeCount' in stats:
            stat_dict = {'commentCount': stats['commentCount'], 'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount'], 'dislikeCount': stats['dislikeCount'], 'likeCount': stats['likeCount']}
        elif 'commentCount' not in stats and 'dislikeCount' not in stats and 'likeCount' not in stats:
            stat_dict = {'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount']}
        elif 'commentCount' in stats and 'dislikeCount' not in stats and 'likeCount' not in stats:
            stat_dict = {'commentCount': stats['commentCount'], 'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount']}
        elif 'commentCount' not in stats and 'dislikeCount' in stats and 'likeCount' in stats:
            stat_dict = {'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount'], 'dislikeCount': stats['dislikeCount'], 'likeCount': stats['likeCount']}

        sts = pd.concat([sts, pd.DataFrame([stat_dict])], ignore_index=True)

    # Create a dataframe that contains the topic categories
    topicDetails = pd.DataFrame(columns = ['topicCategories'])
    df2 = df.dropna().copy()
    for topic in df2['topicDetails']:
        index = 0
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)

    # Create a new dataframe that has attributes of sts and target as the categories
    df3 = sts.head(24272).copy()  # only 24272 records to match number of targets
    df3['target'] = topicDetails['topicCategories'].tolist()
    df3.dropna(inplace=True)

    df4 = df3.copy()
    df4.reset_index(drop=True, inplace=True)  # reset the indices to removes jumps in numbers

    # Assign a label of 1 to the big 5 categories. Label of 0 to everything else.
    for i in range(23245):
        if df4['target'][i] == 'Society' or df4['target'][i] == 'Politics' or df4['target'][i] == 'Lifestyle_(sociology)' or df4['target'][i] == 'Entertainment' or df4['target'][i] == 'Music':
            df4['target'][i] = 1
        else:
            df4['target'][i] = 0

    # Split entire data as follows: 70% training data, 10% validation data, 20% test data
    train = df4.iloc[0:16272]
    val = df4.iloc[16272:18597]
    test = df4.iloc[18597:23245]

    # Split data into a dataframe of attributes and a column of target labels
    x_train = train.drop(columns='target')
    y_train = train['target']
    y_train = y_train.astype('int')

    x_val = val.drop(columns='target')
    y_val = val['target']
    y_val = y_val.astype('int')

    x_test = test.drop(columns='target')
    y_test = test['target']
    y_test = y_test.astype('int')

    # Train a decision tree classifier using the training data
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)
    clf = clf.fit(x_train, y_train)

    # Calculate the accuracies on each dataset
    train_accuracy = 1 - np.sum(np.abs(y_train - clf.predict(x_train))) / x_train.shape[0]
    val_accuracy = 1 - np.sum(np.abs(y_val - clf.predict(x_val))) / x_val.shape[0]
    test_accuracy = 1 - np.sum(np.abs(y_test - clf.predict(x_test))) / x_test.shape[0]

    # Plot the decision tree
    fig = plt.figure(figsize=(15,15))
    dt = sklearn.tree.plot_tree(clf, filled=True, feature_names=x_train.columns, class_names=['Not Big 5', 'Big 5'], fontsize=8)

    return train_accuracy, val_accuracy, test_accuracy, dt
