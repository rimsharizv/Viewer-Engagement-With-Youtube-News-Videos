import pandas as pd

def cleanup():
    # Load the JSON file into a pandas DataFrame
    df = pd.read_json('top_news.json', lines=True)
    df = df.dropna()

    # Index(['topicDetails', 'statistics', 'contentDetails', 'snippet', 'id', 'insights'],

    tds = pd.DataFrame(columns = ['topicCategories'])
    for td in df['topicDetails']:
        td_dict = {'topicCategories': td['topicCategories']}
        tds = pd.concat([tds, pd.DataFrame([td_dict])], ignore_index=True)
    tds.dropna()
    tds.drop_duplicates()

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
    sts.dropna()
    sts.drop_duplicates()

    cds = pd.DataFrame(columns = ['duration', 'definition', 'dimension', 'caption'])
    for cd in df['contentDetails']:
        cd_dict = {'duration': cd['duration'], 'definition': cd['definition'], 'dimension': cd['dimension'], 'caption': cd['caption']}
        cds = pd.concat([cds, pd.DataFrame([cd_dict])], ignore_index=True)
    cds.dropna()
    cds.drop_duplicates()

    snippets = pd.DataFrame(columns = ['description', 'title', 'channelId', 'channelTitle', 'publishedAt', 'categoryId', 'detectLang'])
    for snippet in df['snippet']:
        snippet_dict = {'description': snippet['description'], 'title': snippet['title'], 'channelId': snippet['channelId'], 'channelTitle': snippet['channelTitle'], 'publishedAt': snippet['publishedAt'], 'categoryId': snippet['categoryId'], 'detectLang': snippet['detectLang']}
        snippets = pd.concat([snippets, pd.DataFrame([snippet_dict])], ignore_index=True)
    snippets.dropna()
    snippets.drop_duplicates()

    insts = pd.DataFrame(columns = ['startDate', 'dailyShare'])
    for inst in df['insights']:
        inst_dict = {'startDate': inst['startDate'], 'dailyShare': inst['dailyShare']}
        insts = pd.concat([insts, pd.DataFrame([inst_dict])], ignore_index=True)
    insts.dropna()
    insts.drop_duplicates()

    return tds, sts, cds, snippets, insts
