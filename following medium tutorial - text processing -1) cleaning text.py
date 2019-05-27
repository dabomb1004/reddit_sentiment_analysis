
# coding: utf-8

# In[5]:


import spacy
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
import re
from bs4 import BeautifulSoup
from contractions import CONTRACTION_MAP
import unicodedata

#nlp = spacy.load('en_core', parse=True, tag=True, entity=True)

#nlp_vec = spacy.load('en_vecs', parse = True, tag=True, entity=True)
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list.remove('no')
stopword_list.remove('not')

file = pd.read_csv(r'C:\Users\kim\Downloads\cambridge_analytica_facebook_comments_trimmed.csv')

file = file['body']


def strip_html_tags(text):

    soup = BeautifulSoup(text, "html.parser")

    stripped_text = soup.get_text()

    return stripped_text


def remove_accented_chars(text):

    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    return text


def remove_special_characters(text, remove_digits=False):

    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'

    text = re.sub(pattern, '', text)

    return text

def simple_stemmer(text):

    ps = nltk.porter.PorterStemmer()

    text = ' '.join([ps.stem(word) for word in text.split()])

    return text


def remove_stopwords(text, is_lower_case=False):

    tokens = tokenizer.tokenize(text)

    tokens = [token.strip() for token in tokens]

    if is_lower_case:

        filtered_tokens = [token for token in tokens if token not in stopword_list]

    else:

        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]

    filtered_text = ' '.join(filtered_tokens)    

    return filtered_text

#using all the definitions above


normalized_corpus = []

for doc in file:
    
    doc = str(doc)
    
     # remove accented characters

    doc = remove_accented_chars(doc)

    doc = doc.lower()

    # strip HTML

    doc = strip_html_tags(doc)


    # remove extra newlines

    doc = re.sub(r'[\r|\n|\r\n]+', ' ',doc)

    # lemmatize text

    #if text_lemmatization:

        #doc = lemmatize_text(doc)

    # remove special characters and\or digits    


        # insert spaces between special characters to isolate them    

    special_char_pattern = re.compile(r'([{.(-)!}])')

    doc = special_char_pattern.sub(" \\1 ", doc)

    doc = remove_special_characters(doc, remove_digits=True)  

    # remove extra whitespace

    doc = re.sub(' +', ' ', doc)

    # remove stopwords


    doc = remove_stopwords(doc, is_lower_case=True)



    normalized_corpus.append(doc)
   


#pre-process text and store the same

data = pd.DataFrame(normalized_corpus, columns=['clean_text'])

data.to_csv(r'C:\Users\kim\Documents\cambridge_analytica_facebook_comments_CLEANED.csv')

