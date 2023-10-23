import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def makeChart2():
    df = pd.read_json('top_news.json', lines=True)
    topicDetails = pd.DataFrame(columns = ['topicCategories'])
    df2 = df.dropna()
    for topic in df2['topicDetails']:
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)
    #topicDetails
    snippets = pd.DataFrame(columns = ['description', 'title', 'channelId', 'channelTitle', 'publishedAt', 'categoryId', 'detectLang'])
    for snippet in df2['snippet']:
        snippet_dict = {'description': snippet['description'], 'title': snippet['title'], 'channelId': snippet['channelId'], 'channelTitle': snippet['channelTitle'], 'publishedAt': snippet['publishedAt'], 'categoryId': snippet['categoryId'], 'detectLang': snippet['detectLang']}
        snippets = pd.concat([snippets, pd.DataFrame([snippet_dict])], ignore_index=True)
    #snippets
    insights = pd.DataFrame(columns = ['totalView'])
    for insight in df2['insights']:
        insight_dict = {'totalView': insight['totalView']}
        insights = pd.concat([insights, pd.DataFrame([insight_dict])], ignore_index=True)
    #insights
    combinedNew = pd.concat([snippets, insights, topicDetails], axis=1)
    combinedNew
    combinedNew2 = combinedNew
    combinedNew2 = combinedNew2[combinedNew2["topicCategories"].str.contains("Entertainment")]
    combinedNew2["totalView"] = combinedNew2["totalView"].apply(np.int64)
    combinedNew2
    ax = sns.boxplot(data=combinedNew2, x="totalView")
    plt.xscale('log')
    plt.xlabel("Total Views for 'Entertainment' Category (Logarithmic)")
    
def makeChart3():
    df = pd.read_json('top_news.json', lines=True)
    topicDetails = pd.DataFrame(columns = ['topicCategories'])
    df2 = df.dropna()
    for topic in df2['topicDetails']:
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)
    #topicDetails
    snippets = pd.DataFrame(columns = ['description', 'title', 'channelId', 'channelTitle', 'publishedAt', 'categoryId', 'detectLang'])
    for snippet in df2['snippet']:
        snippet_dict = {'description': snippet['description'], 'title': snippet['title'], 'channelId': snippet['channelId'], 'channelTitle': snippet['channelTitle'], 'publishedAt': snippet['publishedAt'], 'categoryId': snippet['categoryId'], 'detectLang': snippet['detectLang']}
        snippets = pd.concat([snippets, pd.DataFrame([snippet_dict])], ignore_index=True)
    #snippets
    insights = pd.DataFrame(columns = ['totalView'])
    for insight in df2['insights']:
        insight_dict = {'totalView': insight['totalView']}
        insights = pd.concat([insights, pd.DataFrame([insight_dict])], ignore_index=True)
    #insights
    combinedNew = pd.concat([snippets, insights, topicDetails], axis=1)
    combinedNew
    combinedNew2 = combinedNew
    combinedNew2 = combinedNew2[combinedNew2["topicCategories"].str.contains("Politics")]
    combinedNew2["totalView"] = combinedNew2["totalView"].apply(np.int64)
    combinedNew2
    ax = sns.boxplot(data=combinedNew2, x="totalView")
    plt.xscale('log')
    plt.xlabel("Total Views for 'Politics' Category (Logarithmic)")