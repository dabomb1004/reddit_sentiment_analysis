
# coding: utf-8

# In[12]:


import pandas as pd


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from datetime import datetime
import praw
import requests

#import urllib.request
#in case chrome tries to block it

options = Options()
options.add_argument('--disable-infobars')

options.add_argument("--start-maximized")


#locate folder where exe is in
browser = webdriver.Chrome(r'C:\Users\dankim123\Documents\chromedriver.exe', options = options)

document = pd.read_csv(r'C:\Users\dankim123\Documents\USELECTION_unfiltered.csv')
#document = document[624:629]



links = document['full_link']


reddit = praw.Reddit(client_id='I7RmMPzvKDtZFQ',
                         client_secret='BQ0q4IanqFiGvC_pvw7i2PHeHPg',
                         user_agent='goldenhen')

#starting from this place


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
                time.sleep(.5)
                print(tally)
                print(count)
        
    
        



        
information = {'link_title': link_title, 'author': list1, 'body': list2, 'date': list3, 'distinguished': list4, 'edited': list5, 'id':list6,
          'is_submitter': list7, 'link_id': list8, 'parent_id': list9, 'permalink': list10, 'replies': list11, 'score': list12
          , 'stickied': list13, 'submission': list14, 'subreddit': list15, 'subreddit_id': list16}

df = pd.DataFrame.from_dict(information)


df.to_csv(r'C:\Users\dankim123\Documents\brexit_comments_{}.csv'.format('trimmed1'))


# In[6]:


link_title = link_title[0:200000]
list0 = list0[0:200000]
list1 = list1[0:200000]
list2 = list2[0:200000]
list3 = list3[0:200000]
list4 = list4[0:200000]
list5 = list5[0:200000]
list6 = list6[0:200000]
list7 = list7[0:200000]
list8 = list8[0:200000]
list9 = list9[0:200000]
list10 = list10[0:200000]
list11 = list11[0:200000]
list12 = list12[0:200000]


information = {'link_title': link_title, 'author': list1, 'body': list2, 'date': list3, 'distinguished': list4, 'edited': list5, 'id':list6,
          'is_submitter': list7, 'link_id': list8, 'parent_id': list9, 'permalink': list10, 'replies': list11, 'score': list12
          , 'stickied': list13, 'submission': list14, 'subreddit': list15, 'subreddit_id': list16}

df = pd.DataFrame.from_dict(information)


df.to_csv(r'C:\Users\dankim123\Documents\brexit{}.csv'.format('_comments7'))


# In[1]:


import pandas as pd


document = pd.read_csv(r'C:\Users\kim\Documents\brexit_Score_start_to_56009.csv', low_memory = False)
#document = document[624:629]



document.index[document['body']==].tolist()


# In[3]:


information = {'link_title': link_title, 'author': list1, 'body': list2, 'date': list3, 'distinguished': list4, 'edited': list5, 'id':list6,
          'is_submitter': list7, 'link_id': list8, 'parent_id': list9, 'permalink': list10, 'replies': list11, 'score': list12
          , 'stickied': list13, 'submission': list14, 'subreddit': list15, 'subreddit_id': list16}

df = pd.DataFrame.from_dict(information)


df.to_csv(r'C:\Users\dankim123\Documents\fb_ca{}.csv'.format('_comments3'))


# In[17]:


import pandas as pd


document = pd.read_csv(r'C:\Users\kim\Documents\brexit.csv')

document['created_utc'] = pd.to_datetime(document['created_utc'])  
#document = document[250:1582]
mask = (document['created_utc'] > '6/9/2016') & (document['created_utc'] < '7/8/2016')
document = document.loc[mask]

document = document[document['full_link'].str.contains('brexit|eu|referendum|freedom|exit|leave|union|ttip|nhs|immigration|voters|vote')]

document.to_csv(r'C:\Users\kim\Documents\brexit_specific_words.csv')


# In[9]:


import pandas as pd


document = pd.read_csv(r'C:\Users\dankim123\Documents\cambridge_analytica_facebook.csv')

document['date'] = pd.to_datetime(document['date'])  

mask = (document['date'] > '3/3/2018') & (document['date'] <= '3/31/2018')
document = document.loc[mask]

document = document[document['permalink'].str.contains('facebook|cambridge analytica|wylie|kogan|privacy|election|russia')]

document.to_csv(r'C:\Users\kim\Documents\cambridge_analytica_facebook_comments_trimmed.csv')
print(len(document))


# In[3]:


import pandas as pd


document = pd.read_csv(r'C:\Users\kim\Pictures\project\reddit\facebook ca\Facebook_Scorecheck_start_to_end.csv')

document['date'] = pd.to_datetime(document['date'])  

document.drop_duplicates(subset='body', keep=False)
when= (document['date'] > '3/23/2018') & (document['date'] <= '4/24/2018')
document = document.loc[when]

#document = document[document['permalink'].str.contains('facebook|cambridge analytica|wylie|kogan|privacy|election|russia')]

document.to_csv(r'C:\Users\kim\Documents\FACEBOOK_Hearing.csv')
print(len(document))


# In[11]:


import pandas as pd


document = pd.read_csv(r'C:\Users\dankim123\Documents\cambridge_analytica_facebook_comments_trimmed.csv')

df.groupby(['date']).count()


# In[20]:


import pandas as pd


document = pd.read_csv(r'C:\Users\kim\Documents\uselection2016_Oct_to_Nov_filtered_threads.csv')
document.dropna

document['created_utc'] = pd.to_datetime(document['created_utc'])  

#interval = (document['created_utc'] > '10/24/2016') & (document['created_utc'] <= '11/23/2016')
#document = document.loc[interval]
document = document[document['full_link'].str.contains('election|us election 2016|trump|hillary|president|democrats|republicans|polling|voting|vote|race|election|elect|vote|presidential|candidate')]


document.to_csv(r'C:\Users\kim\Documents\USELECTION_filtered.csv')


# In[1]:


import pandas as pd 
import numpy as np

document = pd.read_csv(r'C:\Users\kim\Documents\facebook_march03_march14_threads.csv')
document['body'].replace('none', np.nan, inplace=True)
document['date'] = pd.to_datetime(document['date'])  

interval = (document['date'] > '03/16/2018') & (document['date'] < '06/06/2018')
document.dropna(subset=['body'], inplace=True)
document = document.loc[interval]

document = document[document['body'].str.contains('mercer | eu hearing | policy | Aleksandr Kogan | Putin |parliament | interference| stolen| personal | data| facebook | Zuckerberg | stock price | warning | ca | zuck | psychographic | segment | Cambridge Analytica| Analytica| Mark Zuckerberg | data breach | privacy | violation | Facebook | cambridge analytica| kogan | russia | Data | regulation | washington | hearing | wylie | sheryl | profile | profiles | eu | data policy | breach | deletefacebook | fb | cybersecurity | misuse | apology | press release ')]


document.to_csv(r'C:\Users\kim\Documents\facebook_march03_march14_threads_filtered.csv')


# In[16]:


import pandas as pd 
import numpy as np

document = pd.read_csv(r'C:\Users\kim\Documents\Hazar2.csv', encoding = "ISO-8859-1")

document['Document'] = document['Document'].apply(lambda x:" ".join(str(x).lower() for x in x.split()))

document = document[document['Document'].str.contains("bed | stay | hotel | room | price | Hotel | location| lounge | Inn")]
document.to_csv(r'C:\Users\kim\Documents\Hazar2_filtered2.csv', encoding = "utf-8")


# In[21]:


import pandas as pd 
import numpy as np

#take random sample from dataset 

df = pd.read_csv(r'C:\Users\kim\Documents\USELECTION_filtered.csv')

df = df.groupby('date').apply(lambda x: x.sample(3, replace=True)).reset_index(drop=True)
print(df)
df.drop_duplicates()

df.to_csv(r'C:\Users\kim\Documents\USELECTION_RANDOM_SELECTION.csv')


# In[22]:


import pandas as pd 
import numpy as np

df = pd.read_csv(r'C:\Users\kim\Documents\FACEBOOK_HEARING.csv')

df.subreddit = pd.Categorical(df.subreddit)

df['subreddit_code'] = df.subreddit.cat.codes

df.author = pd.Categorical(df.author)
df.link_title = pd.Categorical(df.link_title)

df['link_title_code'] = df.link_title.cat.codes
df['author_code'] = df.author.cat.codes


df.to_csv(r'C:\Users\kim\Documents\FACEBOOK_HEARING_CATEGORIZED.csv')

