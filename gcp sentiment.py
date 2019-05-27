
# coding: utf-8

# In[ ]:


from google.cloud import language
import pandas as pd 
import time


client = language.LanguageServiceClient.from_service_account_json(r'C:\Users\kim\Downloads\My First Project-7f8c6a198cb1.json')

dataset = pd.read_csv(r'C:\Users\kim\Documents\FACEBOOK_Hearing.csv')   # ----------------source file 

#dataset = dataset[39759:]

#dataset = dataset[1:12]


    
    
    #authenticate    put json file inside folder 
    
#YOU'RE AUTHENTICATED!
def gc_sentiment(text):  
   

    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    
   
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude, text






#[0:779]   --or delete 5581






text = dataset['body']



score = []
mag = []
box = []
bins = []
reddit_score = []
date = []
link_title = []
author = []

count = 0           
for row in text:
    
    #THIS IS NOT WORKING!
    try:
        print(row)
        row = str(row)
        sentiment = gc_sentiment(row)
        
            
            
        score.append(sentiment[0])
        mag.append(sentiment[1])
        box.append(sentiment[2])
        
        string = str(sentiment[2])
        
        i = dataset.index[dataset['body']== string].tolist()
        i = int(i[0])
        print(i)
        
        bins.append(dataset['subreddit'][i])
        reddit_score.append(dataset['score'][i])
        date.append(dataset['date'][i])
        link_title.append(dataset['link_title'][i])
        author.append(dataset['author'][i])
        
        
        print(gc_sentiment(row))

        time.sleep(.07)
        
        


        count+=1
        print(count)
        
    except:
        continue
        print('didnt work')
        score.append('none')
        mag.append('none')
        


#gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists



columns = ['score']
gc_df1 = pd.DataFrame(score, columns = columns)
columns = ['mag']
gc_df2 = pd.DataFrame(mag, columns=columns)
columns = ['text']
gc_df3 = pd.DataFrame(box, columns=columns)
columns = ['subreddit']
gc_df4 = pd.DataFrame(bins, columns=columns)
columns = ['date']
gc_df5 = pd.DataFrame(date, columns=columns)
columns = ['link_title']
gc_df6 = pd.DataFrame(link_title, columns=columns)
columns = ['author']
gc_df7 = pd.DataFrame(author, columns=columns)
columns = ['reddit_score']
gc_df8 = pd.DataFrame(reddit_score, columns=columns)


        

gc_df = pd.concat([gc_df1,gc_df2, gc_df3, gc_df4, gc_df5, gc_df6, gc_df7, gc_df8], axis=1, sort=False)

gc_df.to_csv(r'C:\Users\kim\Documents\FACEBOOK_SENTIMENT.csv')



# In[8]:


for x,y in zip([2, 3],[(1,0), (2,0)]):
    print(x, y[0])


# In[4]:


import pandas as pd 



gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists

#creating spreadsheet
gc = list(zip(gc_score, gc_magnitude))
columns = ['score', 'magnitude']
gc_df = pd.DataFrame(gc, columns = columns)



gc_df.to_csv(r'C:\Users\kim\Documents\brexit_56009.csv')


# In[36]:


from google.cloud import language
import pandas as pd 
import time


client = language.LanguageServiceClient.from_service_account_json(r'C:\Users\kim\Downloads\My First Project-7f8c6a198cb1.json')

dataset = pd.read_csv(r'C:\Users\kim\Pictures\project\twitter\facebook ca\Twitter_CA_filtered.csv')   # ----------------source file 

#dataset = dataset[39759:]

dataset = dataset[1:12]


    
    
    #authenticate    put json file inside folder 
    
#YOU'RE AUTHENTICATED!
def gc_sentiment(text):  
   

    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    
   
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude, text






#[0:779]   --or delete 5581






text = dataset['tweets_content']

score = []
mag = []
tweets_content = []



Keywords = []
tweets_about = []
tweets_at_name = []
tweets_date = []
tweets_following = []
tweets_followers = []
tweets_joined = []
tweets_likes = []
tweets_location = []
tweets_msg = []
tweets_tweets= []
tweets_responses = []
tweets_name = []


count = 0           
for row in text:
    
    #THIS IS NOT WORKING!
    try:
        print(row)
        row = str(row)
        sentiment = gc_sentiment(row)
        
            
            
        score.append(sentiment[0])
        mag.append(sentiment[1])
        tweets_content.append(sentiment[2])
        
        string = str(sentiment[2])
        
        i = dataset.index[dataset['tweets_content']== string].tolist()
        i = int(i[0])
        print(i)
        

        Keywords.append(dataset['Keywords'][i])
        tweets_about.append(dataset['tweets_about'][i]) 
        tweets_date.append(dateset['tweets_date'][i])
        tweets_at_name.append(dataset['tweets_at_name'][i])
        tweets_followers.append(dataset['tweets_followers'][i])
        tweets_following.append(dataset['tweets_following'][i])
        
       
        tweets_joined.append(dataset['tweets_joined'][i])
        tweets_likes.append(dataset['tweets_likes'][i])
  
        tweets_location.append(dataset['tweets_location'][i])
        tweets_msg.append(dataset['tweets_msg'][i])
        tweets_name.append(dataset['tweets_name'][i])
        tweets_tweets.append(dataset['tweets_tweets'][i])
        tweets_retweets.append(dataset['tweets_responses'][i])
       
        
        
        print(gc_sentiment(row))

        time.sleep(.03)
        
        


        count+=1
        print(count)
        
    except:
        continue
        print('didnt work')
        score.append('none')
        mag.append('none')
    
    time.sleep(.03)
        


#gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists

#words = [score, mag, tweets_content, Keywords,tweets_about, tweets_at, tweets_following, tweets_followers, tweets_joined,tweets_likes, tweets_location, tweets_msg, tweets_tweets, tweets_retweets]
#columns = []
#for x in ['score', 'mag', 'tweets_content','Keywords', 'tweets_about','tweets_at','tweets_following', 'tweets_followers','tweets_joined', 'tweets_likes','tweets_location', 'tweets_msg', 'tweets_tweets','tweets_retweets']:
#    columns.append(x)
#lists= []


gc_df1 = pd.DataFrame(score, columns = ["sentiment"])
gc_df2 = pd.DataFrame(mag, columns = ["mag"])
gc_df3 = pd.DataFrame(tweets_content, columns = ["tweets_content"])
gc_df4 = pd.DataFrame(Keywords, columns = ["Keywords"])
gc_df5 = pd.DataFrame(tweets_about, columns =["tweets_about"])
gc_df6 = pd.DataFrame(tweets_at_name, columns = ["@name"])
gc_df7 = pd.DataFrame(tweets_following, columns = ["following"] )
gc_df8 = pd.DataFrame(tweets_followers, columns = ["followers"])
gc_df9 = pd.DataFrame(tweets_joined, columns = ["tweets_joined"])
gc_df10 = pd.DataFrame(tweets_likes, columns = ["likes"])
gc_df11 = pd.DataFrame(tweets_location, columns =[ "location"])
gc_df12 = pd.DataFrame(tweets_msg, columns = ["msg"])
gc_df13 = pd.DataFrame(tweets_tweets, columns = ["total_tweets"])
gc_df14 = pd.DataFrame(tweets_responses, columns = ["responses"])
gc_df15 = pd.DataFrame(tweets_date, columns= ["date"])
gc_df16 = pd.DataFrame(tweets_name, columns=['name'])

print(gc_df10)

gc_df = pd.concat([gc_df1, gc_df2, gc_df3, gc_df4, gc_df5, gc_df6, gc_df7, gc_df8, gc_df9, gc_df10, gc_df11, gc_df12, gc_df13, gc_df14, gc_df16, gc_df15], axis=1, sort=False)  





        



gc_df.to_csv(r'C:\Users\kim\Documents\twitter_facebookCA_sentiment_test.csv')



# In[26]:


print(tweets_about)


# In[15]:



import pandas as pd




dataset = pd.read_csv(r'C:\Users\kim\Documents\cambridge_analytica_facebook_comments_CLEANED.csv')

dataset2 = pd.read_csv(r'C:\Users\kim\Downloads\cambridge_analytica_facebook_comments_trimmed.csv')

data_combined = pd.concat([dataset, dataset2], axis=1, sort=False)

data_combined.drop_duplicates()

data_combined.dropna

data_combined.to_csv(r'C:\Users\kim\Documents\facebook_CA_final_sheet.csv')


# In[74]:


import pandas as pd




dataset = pd.read_csv(r'C:\Users\kim\Documents\cambridge_analytica_facebook_comments_CLEANED.csv')

dataset2 = pd.read_csv(r'C:\Users\kim\Downloads\cambridge_analytica_facebook_comments_trimmed.csv')

dataset = dataset[2:10]

dataset2 = dataset2[2:10]


import nltk
from textblob import TextBlob
nltk.download('words')

words = set(nltk.corpus.words.words())
dataset2['body'] = dataset2['body'].apply(lambda x:"".join(w for w in x          if w.lower() is not w.isalpha()))

sentiment_scores_tb = [round(TextBlob(str(article)).sentiment.polarity, 3) for article in dataset2['body']]

from google.cloud import language

import time

#YOU'RE AUTHENTICATED!
def gc_sentiment(text):  
   
    from google.cloud import language
    
    #authenticate
    client = language.LanguageServiceClient.from_service_account_json(r'C:\Users\kim\Downloads\sentiment-234614-fb3ce044196c.json')
    
    
    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    
   
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude




import pandas as pd
from langdetect import detect 
import re
import nltk
from nltk.corpus import stopwords


stop = stopwords.words('english')

text = dataset['clean_text']

text2 = dataset2['body']


gc_results = []
gc_results2 =[]
count = 0           
for row in text:
    
    
    try:
        print(row)
        row = str(row)
        gc_results.append(gc_sentiment(row))

        time.sleep(.3)



        count+=1
        print(count)
        
    except InvalidArgument:
        continue
        
count = 0           
for row in text2:
    
    
    try:
        print(row)
        row = str(row)
        gc_results2.append(gc_sentiment(row))

        time.sleep(.3)



        count+=1
        print(count)
        
    except InvalidArgument:
        continue

gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists

#creating spreadsheet
gc = list(zip(gc_score, gc_magnitude))
columns = ['score', 'magnitude']
gc_df = pd.DataFrame(gc, columns = columns)

gc_score, gc_magnitude = zip(*gc_results2) # Unpacking the result into 2 lists

#creating spreadsheet
gc2 = list(zip(gc_score, gc_magnitude))
columns = ['score', 'magnitude']
gc_df2 = pd.DataFrame(gc2, columns = columns)






gc_df.to_csv(r'C:\Users\kim\Documents\score_comparison.csv')

gc_df2.to_csv(r'C:\Users\kim\Documents\score_comparison2.csv')

print(sentiment_scores_tb)


# In[29]:


import pandas as pd

df1 = pd.read_csv(r'C:\Users\kim\Documents\facebook_EDITED.csv')

df2 = pd.read_csv(r'C:\Users\kim\Downloads\cambridge_analytica_facebook_comments_trimmed.csv')

df2.loc[~df2.edited.isin(df1.edited)]


# In[43]:


#7613

import pandas as pd


#[0:779]   --or delete 5581


compare = pd.read_csv(r'C:\Users\kim\Downloads\brexit_comments_sentiment_redo.csv') 
df = pd.read_csv(r'C:\Users\kim\Downloads\BREXIT_COMMENTS_FINAL.csv')




text = compare['text']

count = 1 

for x in text:
    
    
    try:
        string = str(x)
        
        i = df.index[df['body']== string].tolist()
        print(i)
        
        if len(i) >0:
            print(string)
            
        i = int(i[0])
        print(i)
        
        
        e = compare.index[compare['text'] == string].tolist()
        e = int(e[0])
        print(e)
      
        
        compare['link_title'][e] = df['link_title'][i]
        compare['author'][e] = df['author'][i]
        compare['date'][e] = df['date'][i]
       
        
        compare['reddit_score'][e] = df['score'][i]
        compare['subreddit'][e] = df['subreddit'][i]
    except IndexError:
        continue



df.to_csv(r'C:\Users\kim\Documents\BREXIT_SENTIMENT_REDONE.csv')


# In[44]:


compare.to_csv(r'C:\Users\kim\Downloads\brexit_comments_sentiment_redo22.csv') 


# In[ ]:


#7613

import pandas as pd


#[0:779]   --or delete 5581


compare = pd.read_csv(r'C:\Users\kim\Downloads\brexit_comments_sentiment_redo.csv') 
df = pd.read_csv(r'C:\Users\kim\Downloads\BREXIT_COMMENTS_FINAL.csv')




text = compare['text']

count = 1 

for x in text:
    
    
    try:
        string = str(x)
        
        i = df.index[df['body']== string].tolist()
        print(i)
        
        if len(i) >0:
            print(string)
            
        i = int(i[0])
        print(i)
        
        
        e = compare.index[compare['text'] == string].tolist()
        e = int(e[0])
        print(e)
      
        
        compare['link_title'][e] = df['link_title'][i]
        compare['author'][e] = df['author'][i]
        compare['date'][e] = df['date'][i]
       
        
        compare['reddit_score'][e] = df['score'][i]
        compare['subreddit'] = df['subreddit'][i]
        
        compare['tweets_date'][e]= df['tweets_date'][i]
        compare['tweets_at_name'][e] =df['tweets_at_name'][i]
        compare['tweets_followers'][e] = df['tweets_followers'][i]
        compare['tweets_following'][e] =df['tweets_following'][i]
        
       
        compare['tweets_joined'][e] = df['tweets_joined'][i]
        compare['tweets_likes'][e] = df['tweets_likes'][i]
  
        comapare['tweets_location'][e] = df['tweets_location'][i]
        compare['tweets_msg'][e] = df['tweets_msg'][i]
        comapre['tweets_name'][e] = df['tweets_name'][i]
        compare['tweets_tweets'][e] = df['tweets_tweets'][i]
        compare['tweets_responses'][e] = df['tweets_responses'][i]
       
    except IndexError:
        continue



df.to_csv(r'C:\Users\kim\Documents\BREXIT_SENTIMENT_REDONE.csv')

