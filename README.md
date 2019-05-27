# reddit_sentiment_analysis
cleaning reddit comments and analyzing them
The overall order is 

#first getting the raw data from reddit - events were: US electionn 2016, Brexit ref 2016, Facebook Cambridge Analytica 2018

1. pushshift - getting reddit threads for specific topic
2. pushshift - getting comments for each thread

#next taking out any unncessary words or unrelated words to specific event

3. filtering

#finally using google cloud platform to get sentiment score for each comment

4. gcp sentiment

#on the side I did a different apporach to sentiment analysis using textblob instead of gcp sentiment

5. following medium tutorial - text processing -cleaning text

6. following medium tutorial - text processing - analyzing

#there is a final text analysis .py file that I used to try and play around with the data. I followed a tutorial and cleaned the
#words using their approach and created a word cloud at the end. 

7. text analysis 

