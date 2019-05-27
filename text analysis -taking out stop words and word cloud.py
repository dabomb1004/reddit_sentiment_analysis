
# coding: utf-8

# In[19]:


#C:\Users\kim\Documents\brexit_comments1.csv

import gensim 
import pandas as pd
from gensim import corpora

comments = pd.read_csv(r'C:\Users\kim\Documents\brexit_comments1.csv')

comments = comments[1:189278]

text = comments['body']

try:
    text = text.apply(lambda x: " ".join(x.lower() for x in str(x).split()))
    
except AttributeError:
    print("'float' object has no attribute 'split'")
    
text = text.str.replace('[^\w\s]','')

from nltk.corpus import stopwords
stop = stopwords.words('english')
text = text.apply(lambda x: " ".join(x for x in x.split() if x not in stop))

freq = pd.Series(' '.join(text).split()).value_counts()[:15]

freq = list(freq.index)

text = text.apply(lambda x: " ".join(x for x in x.split() if x not in freq))



from nltk.stem import PorterStemmer

st = PorterStemmer()
text = text.apply(lambda x: " ".join([st.stem(word) for word in x.split()]))


from textblob import TextBlob

#tf1 = (text[1:2]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
#tf1.columns = ['words','tf']

#print(tf1)
    
#from gensim.summarization import summarize

#print(text)
#summarize(text)

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


count_vectorizer = CountVectorizer(ngram_range=(1, 2),  
                                   stop_words='english', 
                                   token_pattern="\\b[a-z][a-z]+\\b",
                                   lowercase=True,
                                   max_df = 0.6, max_features=4000)
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2),  
                                   stop_words='english', 
                                   token_pattern="\\b[a-z][a-z]+\\b",
                                   lowercase=True,
                                   max_df = 0.6, max_features=4000)

cv_data = count_vectorizer.fit_transform(text)
tfidf_data = tfidf_vectorizer.fit_transform(text)

import wordcloud 
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

for_wordcloud = count_vectorizer.get_feature_names()

for_wordcloud_str = ' '.join(for_wordcloud)

wordcloud = WordCloud(width=800, height=400, background_color ='black',
                      min_font_size = 7).generate(for_wordcloud_str)

plt.figure(figsize=(20, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
 
plt.show()


# try using 10 dimensions
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
import sklearn

n_comp = 10
lsa_tfidf = TruncatedSVD(n_components=n_comp)
lsa_cv = TruncatedSVD(n_components=n_comp)
nmf_tfidf = NMF(n_components=n_comp)
nmf_cv = NMF(n_components=n_comp)

lsa_tfidf_data = lsa_tfidf.fit_transform(tfidf_data)
lsa_cv_data = lsa_cv.fit_transform(cv_data)
nmf_tfidf_data = nmf_tfidf.fit_transform(tfidf_data)
nmf_cv_data = nmf_cv.fit_transform(cv_data)


print(lsa_tfidf_data)
print(lsa_cv_data )
print(nmf_tfidf_data)
print(nmf_cv_data)


# In[11]:


import gensim 
import pandas as pd
from gensim import corpora

comments = pd.read_csv(r'C:\Users\kim\Documents\brexit_comments1.csv')
print(len(comments))


# In[23]:


print(lsa_tfidf_data[0])
print(lsa_cv_data )
print(nmf_tfidf_data)
print(nmf_cv_data)

