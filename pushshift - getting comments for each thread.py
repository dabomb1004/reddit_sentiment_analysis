
# coding: utf-8

# In[ ]:


import pandas as pd


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from datetime import datetime
import praw
import requests

import pandas as pd

import urllib.request
#in case chrome tries to block it

options = Options()
options.add_argument('--disable-infobars')

options.add_argument("--start-maximized")


#locate folder where exe is in
browser = webdriver.Chrome(r'C:\Program Files\chromedriver.exe', options = options)

document = pd.read_csv(r'C:\Users\kim\Documents\USELECTION_RANDOM_SELECTION_THREADS.csv')
#document = document[593:]

#document.drop(160)

#document = document[54:]

links = document['full_link']


reddit = praw.Reddit(client_id='I7RmMPzvKDtZFQ',
                         client_secret='BQ0q4IanqFiGvC_pvw7i2PHeHPg',
                         user_agent='goldenhen')

link_title = []
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
#open website



tally = 0 

for link in links: 
    

    browser.get(link)
    
    banned = browser.find_elements_by_xpath("//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[2]/div/div/div[1]/div/div/img")
    
    
    forbidden = browser.find_elements_by_xpath('//*[@id="classy-error"]')
    
    permission = browser.find_elements_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div[1]/div/div/h3')
    
    print('yeah')
    
    if len(banned) > 0:
        print('banned')
        
    elif len(forbidden) > 0:
        print('forbidden')
    
    elif len(permission) > 0:
        print('need permission')
        
    else:

        
        
        stupid = reddit.submission(url= link)

        stupid.comments.replace_more(limit=None)

        count = 1 

        for comment in stupid.comments.list():
            if count ==0:
                pass

            else:


                link_title.append(link)
                list1.append(comment.author)
                list2.append(comment.body)

                #for the time to convert to readable format



                list3.append(datetime.utcfromtimestamp(comment.created_utc))

                list4.append(comment.distinguished)
                list5.append(comment.edited)
                list6.append(comment.id)
                list7.append(comment.is_submitter)
                list8.append(comment.link_id)
                list9.append(comment.parent_id)
                list10.append(comment.permalink)
                list11.append(comment.replies)
                list12.append(comment.score)
                list13.append(comment.stickied)
                list14.append(comment.submission)
                list15.append(comment.subreddit)
                list16.append(comment.subreddit_id)

                tally +=1
                count+=1
                print(tally)
              
                time.sleep(.10)




        
information = {'link_title': link_title, 'author': list1, 'body': list2, 'date': list3, 'distinguished': list4, 'edited': list5, 'id':list6,
          'is_submitter': list7, 'link_id': list8, 'parent_id': list9, 'permalink': list10, 'replies': list11, 'score': list12
          , 'stickied': list13, 'submission': list14, 'subreddit': list15, 'subreddit_id': list16}

df = pd.DataFrame.from_dict(information)


df.to_csv(r'C:\Users\kim\Documents\election2016_random_selected2{}.csv'.format('_COMMENTS'))


# In[ ]:


information = {'link_title': link_title, 'author': list1, 'body': list2, 'date': list3, 'distinguished': list4, 'edited': list5, 'id':list6,
          'is_submitter': list7, 'link_id': list8, 'parent_id': list9, 'permalink': list10, 'replies': list11, 'score': list12
          , 'stickied': list13, 'submission': list14, 'subreddit': list15, 'subreddit_id': list16}

df = pd.DataFrame.from_dict(information)


df.to_csv(r'C:\Users\kim\Documents\USELECTION{}.csv'.format('_COMMENTS_62593'))


# In[3]:


document[document['full_link'] =='https://www.reddit.com/r/politics/comments/59ume4/poll_trump_chipping_away_at_clintons_lead/' ].index.tolist()
      



# In[12]:


#7613

import pandas as pd


#[0:779]   --or delete 5581


dataset = pd.read_csv(r'C:\Users\kim\Documents\brexit_Scorecheck_start_to_end.csv')
dataset[dataset['link_title'] =='https://www.reddit.com/r/news/comments/4ktdm2/google_hq_raided_in_paris_eur_16bn_tax_fraud/' ].index.tolist()

