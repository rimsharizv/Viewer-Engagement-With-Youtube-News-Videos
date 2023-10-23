import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def knn_analysis():
    # Load the data from top_news.json
    df = pd.read_json('top_news.json', lines=True)

    # Creating the statistics dataframe from the original dataframe
    sts = pd.DataFrame(columns=['commentCount'])
    for stats in df['statistics']:
        if 'commentCount' in stats:
            stat_dict = {'commentCount': stats['commentCount']}
            sts = pd.concat([sts, pd.DataFrame([stat_dict])], ignore_index=True)

    # Creating a dataframe that contains the topic categories
    topicDetails = pd.DataFrame(columns=['topicCategories'])
    df2 = df.dropna().copy()
    for topic in df2['topicDetails']:
        index = 0
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)

    # Creating a new dataframe that has attributes of sts and target as the categories
    df3 = sts.head(len(topicDetails)).copy()
    df3['target'] = topicDetails['topicCategories'].tolist()
    df3.dropna(inplace=True)

    # Spliting data into a dataframe of attributes and a column of target labels
    x = df3.drop(columns='target')
    y = df3['target']

    # Converting target labels to numerical values
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Scaling the data
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Training a KNN classifier
    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(x_train, y_train)

    # Predicting the topicCategories based on the commentCount in the test set
    y_pred = clf.predict(x_test)

    # Calculating the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Ploting the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, cmap="BuGn", xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.title("Confusion Matrix")
    plt.show()

    return accuracy
