import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def makeGraph():
    df = pd.read_json('top_news.json', lines=True)
    #snippets = pd.DataFrame(columns = ['description', 'title', 'channelId', 'channelTitle', 'publishedAt', 'categoryId', 'detectLang'])
    #for snippet in df['snippet']:
    #    snippet_dict = {'description': snippet['description'], 'title': snippet['title'], 'channelId': snippet['channelId'], 'channelTitle': snippet['channelTitle'], 'publishedAt': snippet['publishedAt'], 'categoryId': snippet['categoryId'], 'detectLang': snippet['detectLang']}
    #    snippets = pd.concat([snippets, pd.DataFrame([snippet_dict])], ignore_index=True)
    #snippets.head()

    topicDetails = pd.DataFrame(columns = ['topicCategories'])
    df2 = df.dropna()
    for topic in df2['topicDetails']:
        #print(topic['topicCategories'])
        #print(topic['relevantTopicIds'])
        index = 0
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)
    topicDetails
    #statistics
    #statistics = pd.DataFrame(columns = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount'])
    #df2 = df.dropna()
    #for stats in df2['statistics']:
        #print(stats)
        #if 'commentCount' in stats and 'viewCount' in stats and 'favoriteCount' in stats and 'dislikeCount' in stats and 'likeCount' in stats:
            #stat_dict = {'commentCount': stats['commentCount'], 'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount'], 'dislikeCount': stats['dislikeCount'], 'likeCount': stats['likeCount']}
        #elif 'commentCount' not in stats and 'dislikeCount' not in stats and 'likeCount' not in stats:
            #stat_dict = {'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount']}
        #elif 'commentCount' in stats and 'dislikeCount' not in stats and 'likeCount' not in stats:
            #stat_dict = {'commentCount': stats['commentCount'], 'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount']}
        #elif 'commentCount' not in stats and 'dislikeCount' in stats and 'likeCount' in stats:
            #stat_dict = {'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount'], 'dislikeCount': stats['dislikeCount'], 'likeCount': stats['likeCount']}
       # else:
            #print(stats)
        #statistics = pd.concat([statistics, pd.DataFrame([stat_dict])], ignore_index=True)
    #statistics
    #combined = pd.concat([topicDetails, statistics], axis=1)
    #combined
    #combined2 = combined.where(combined.topicCategories == "Politics")
    #combined2 = combined2.dropna()
    #combined3 = combined2[combined2['viewCount'].astype(int) > 2000]
    #combined3['ratio'] = (combined3['dislikeCount'].astype(int))/(combined3['likeCount'].astype(int))
    topicDetails.value_counts()
    #df.sort_values('Global_Sales').tail(5))
    ax = sns.countplot(data=topicDetails, x="topicCategories",order=topicDetails['topicCategories'].value_counts(ascending=False).iloc[:8].index)
    plt.title("8 Largest Categories in Top News Database")
    plt.xlabel("Topic Categories")
    plt.xticks(ticks=[0,1,2,3,4,5,6,7], labels=['Society', 'Politics', 'Lifestyle', 'Entertain', 'Tele', 'Music', 'Vehicle', 'Film'])
#combined3['ratio'] = combined3['ratio'].astype(int)
#sns.histplot(data=combined3, x="ratio", binrange=(0,1))
#sns.scatterplot(data=combined2, x="likeCount", y="dislikeCount")
#s = pd.Series(["Politics"])
#combined2 = combined.where(s.isin(combined['topicCategories']))

#statistics = pd.DataFrame(columns = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount'])
#topicDetails = pd.DataFrame(columns = ['topicCategories'])
#df2 = df.dropna()
#for x in df2:
#    print(x)
#    topic = x['topicDetails']
#    stats = x['statistics']
#    if 'commentCount' in stats and 'viewCount' in stats and 'favoriteCount' in stats and 'dislikeCount' in stats and 'likeCount' in stats:
#        topic_dict = {'topicCategories': topic['topicCategories']}
#        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)
#        stat_dict = {'commentCount': stats['commentCount'], 'viewCount': stats['viewCount'], 'favoriteCount': stats['favoriteCount'], 'dislikeCount': stats['dislikeCount'], 'likeCount': stats['likeCount']}
#        statistics = pd.concat([statistics, pd.DataFrame([stat_dict])], ignore_index=True)
#topicDetails.head()
#statistics.head()