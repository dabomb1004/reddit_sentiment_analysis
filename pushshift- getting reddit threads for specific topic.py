
# coding: utf-8

# In[1]:


import json
import requests
import pandas as pd
from datetime import datetime

author = []
created_utc = []
domain = []

full_link = []
gilded= []
i_id= []
is_reddit_media_domain= []
is_self= []
is_video= []
num_comments = []
num_crossposts = []
over_18 =[]
parent_whitelist_status = []
permalink = []
pinned = []
post_hint = []
score = []
selftext = []
subreddit = []
subreddit_id = []
subreddit_subscribers = []
subreddit_type = []
thumbnail = []
title = []
urls = []
whitelist_status = []


count = 0 

for number in range(1055, 1026, -1):
    y = number-1
    
    url = "https://api.pushshift.io/reddit/search/comment/?q=%22us%22election%22&after={}d&before={}d&aggs=link_id&size=0&sort=asc".format(number,y)
    r = requests.get(url)
    data = r.json()

    data = json.dumps(data)
    data = json.loads(data)


   

    # converting json dataset from dictionary to dataframe

    for num in range(0, len(data['aggs']['link_id'])):
        
        author.append(data['aggs']['link_id'][num]['data']['author'])
        
        time = data['aggs']['link_id'][num]['data']['created_utc']
        
        created_utc.append(datetime.utcfromtimestamp(time))
        domain.append(data['aggs']['link_id'][num]['data']['domain'])
        full_link.append(data['aggs']['link_id'][num]['data']['full_link'])
        
        
        i_id.append(data['aggs']['link_id'][num]['data']['author'])
        is_reddit_media_domain.append(data['aggs']['link_id'][num]['data']['id'])
        is_self.append(data['aggs']['link_id'][num]['data']['is_self'])
        
        num_comments.append(data['aggs']['link_id'][num]['data']['num_comments'])
        
            
        
        over_18.append(data['aggs']['link_id'][num]['data']['over_18'])
        
        permalink.append(data['aggs']['link_id'][num]['data']['permalink'])
        
       
        score.append(data['aggs']['link_id'][num]['data']['score'])
        
        try:
            selftext.append(data['aggs']['link_id'][num]['data']['selftext'])
            
        except KeyError:
            selftext.append('NaN')
        
        
        subreddit.append(data['aggs']['link_id'][num]['data']['subreddit'])
        subreddit_id.append(data['aggs']['link_id'][num]['data']['subreddit_id'])
        
        try:
            subreddit_subscribers.append(data['aggs']['link_id'][num]['data']['subreddit_subscribers'])
        except KeyError: 
            subreddit_subscribers.append('NaN')
        
        try:
            subreddit_type.append(data['aggs']['link_id'][num]['data']['subreddit_type'])
            
        except KeyError:
            subreddit_subscribers.append('NaN')
            
        thumbnail.append(data['aggs']['link_id'][num]['data']['thumbnail'])
        title.append(data['aggs']['link_id'][num]['data']['title'])
        urls.append(data['aggs']['link_id'][num]['data']['url'])
        
        
        print(count)
        count +=1 
       
       

        


information = {'author':author,

'created_utc': created_utc,
'domain': domain,
'full_link':full_link,

'i_id': i_id,
'is_reddit_media_domain': is_reddit_media_domain,
'is_self': is_self,

'num_comments': num_comments,

'over_18': over_18,

'permalink':permalink,


'score':score,
'selftext':selftext,
'subreddit':subreddit,
'subreddit_id':subreddit_id,
'subreddit_subscribers':subreddit_subscribers,

'thumbnail':thumbnail,
'title':title,
'url':url}

df = pd.DataFrame.from_dict(information)

df.to_csv(r'C:\Users\kim\Documents\2016_thread.csv')


print('got it')


# In[3]:


import pandas as pd 


information = {'author':author,

'created_utc': created_utc,
'domain': domain,
'full_link':full_link,

'i_id': i_id,
'is_reddit_media_domain': is_reddit_media_domain,
'is_self': is_self,

'num_comments': num_comments,

'over_18': over_18,

'permalink':permalink,


'score':score,
'selftext':selftext,
'subreddit':subreddit,
'subreddit_id':subreddit_id,


'thumbnail':thumbnail,
'title':title,
'url':url}

df = pd.DataFrame.from_dict(information)

df.to_csv(r'C:\Users\kim\Documents\USELECTION_unfiltered.csv')

