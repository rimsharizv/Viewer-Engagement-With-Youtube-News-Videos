#!/usr/bin/env python
# coding: utf-8

# In this visualization, we are creating a line graph to illustrate the daily view count of a specific video from the categories: Enterntainment and Politics. The data for this line graph is taken from YouTube's Top News section.
# In order to make the visualization easier to understand, we split the data into weekly view count.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.options.mode.chained_assignment = None

def lineGraphVisualization():
    df = pd.read_json('top_news.json', lines=True)
    topicDetails = pd.DataFrame(columns=['topicCategories'])
    df2 = df.dropna()
    for topic in df2['topicDetails']:
        x = topic['topicCategories'][0]
        topic['topicCategories'] = x.replace("https://en.wikipedia.org/wiki/", "")
        x = topic['topicCategories'][0].replace("hthttps://en.wikipedia.org/wiki/", "")
        topic_dict = {'topicCategories': topic['topicCategories']}
        topicDetails = pd.concat([topicDetails, pd.DataFrame([topic_dict])], ignore_index=True)
    snippets = pd.DataFrame(columns=['description', 'title', 'channelId', 'channelTitle', 'publishedAt', 'categoryId', 'detectLang'])
    for snippet in df2['snippet']:
        snippet_dict = {'description': snippet['description'], 'title': snippet['title'], 'channelId': snippet['channelId'], 'channelTitle': snippet['channelTitle'], 'publishedAt': snippet['publishedAt'], 'categoryId': snippet['categoryId'], 'detectLang': snippet['detectLang']}
        snippets = pd.concat([snippets, pd.DataFrame([snippet_dict])], ignore_index=True)
    insights = pd.DataFrame(columns=['totalView'])
    for insight in df2['insights']:
        insight_dict = {'totalView': insight['totalView']}
        insights = pd.concat([insights, pd.DataFrame([insight_dict])], ignore_index=True)
    combinedNew = pd.concat([snippets, insights, topicDetails], axis=1)

    first_entertainment = combinedNew[combinedNew["topicCategories"] == "Entertainment"].iloc[7]
    first_politics = combinedNew[combinedNew["topicCategories"] == "Politics"].iloc[4]

    daily_views_entertainment = [int(view_count) for view_count in df2.loc[first_entertainment.name]['insights']['dailyView'].split(',')]
    daily_views_politics = [int(view_count) for view_count in df2.loc[first_politics.name]['insights']['dailyView'].split(',')]
    
    # converting daily views into weekly for easier visualization
    weekly_views_entertainment = [sum(daily_views_entertainment[i:i+7]) for i in range(0, len(daily_views_entertainment), 7)]
    weekly_views_politics = [sum(daily_views_politics[i:i+7]) for i in range(0, len(daily_views_politics), 7)]

    # padding the shorter list with zeros when dailyView lengths are different
    if len(weekly_views_entertainment) < len(weekly_views_politics):
        weekly_views_entertainment.extend([0] * (len(weekly_views_politics) - len(weekly_views_entertainment)))
    elif len(weekly_views_politics) < len(weekly_views_entertainment):
        weekly_views_politics.extend([0] * (len(weekly_views_entertainment) - len(weekly_views_politics)))

    weekly_views_df = pd.DataFrame({'Entertainment': weekly_views_entertainment, 'Politics': weekly_views_politics})
    weekly_views_df.plot(kind='line')
    plt.xlabel('Weeks')
    plt.ylabel('Weekly Views')
    plt.title('Weekly Views of a Video from Entertainment and Politics Categories')
    plt.legend(['Entertainment', 'Politics'])
    plt.show()

