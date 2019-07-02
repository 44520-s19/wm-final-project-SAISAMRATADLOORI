# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:19:29 2019

@author: S534568
"""


import numpy as np
import matplotlib.pyplot as plt

import pickle
from nltk_helpers import get_sentiments

from imdb import IMDb

ia=IMDb()


series = ia.get_movie('2085059')


ia.update(series, 'episodes')
sumofRating=0.0
no_of_epsdes=0
rating_avg=[]

for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
       episode = series['episodes'][season_nr][episode_nr]
       if episode.get('rating'):
           sumofRating=sumofRating+episode.get('rating')
       print(episode.get('rating'))
       no_of_epsdes=no_of_epsdes+1
    rating_avg.append(sumofRating/no_of_epsdes)
    sumofRating=0  
    no_of_epsdes=0
        
print(rating_avg)


rating1=[]
rating2=[]
rating3=[]
rating4=[]
rating5=[]



for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
        episode = series['episodes'][season_nr][episode_nr]
        print('episode #%s.%s; rating: %s; votes: %s' %
              (season_nr, episode_nr, episode.get('rating'), episode.get('votes')))
        
for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
        episode = series['episodes'][season_nr][episode_nr]
        if season_nr==1:
            rating1.append(episode.get('rating'))
        if season_nr==2:
            rating2.append(episode.get('rating'))
        if season_nr==3:
            rating3.append(episode.get('rating'))
        if season_nr==4:
            rating4.append(episode.get('rating'))
        if season_nr==5:
            rating5.append(episode.get('rating'))
        
    

print(rating5)

count=0

Season1=['2089051','2089051','2089049','2089050']
Season2=['2290780','2542420','2386296','3973198']
Season3=['5497778','5709242','5709230','4538072','5709234','5709236']
Season4=['5710974','5709250','5710976','5710978','5710984','5058700']
Season5=['8503298','8758202','9053874']

RawReview=[]

counter=0

for season in Season1:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         RawReview.append(review['content'])
         
RawReview1=[]         
for season in Season2:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         RawReview1.append(review['content'])  
         
RawReview2=[]          
for season in Season3:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         RawReview2.append(review['content'])  
         
RawReview3=[]          
for season in Season4:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         RawReview3.append(review['content']) 
         
RawReview4=[]          
for season in Season5:
    movie=ia.get_episode(season)
    reviews=ia.get_movie_reviews(season)
    for review in reviews['data']['reviews']:
         count+=1
         RawReview4.append(review['content']) 
         
         
         
with open('season1.pkl', 'wb') as f:
    pickle.dump(RawReview,f)

with open('season2.pkl', 'wb') as f:
    pickle.dump(RawReview1,f)
    
with open('season3.pkl', 'wb') as f:
    pickle.dump(RawReview2,f)
    
with open('season4.pkl', 'wb') as f:
    pickle.dump(RawReview3,f)
    
with open('season5.pkl', 'wb') as f:
    pickle.dump(RawReview4,f)
#Reading the pickle file

with open('season1.pkl','rb') as f:
    sentis1 =pickle.load(f)

with open('season2.pkl','rb') as f:
    sentis2 =pickle.load(f)
    
with open('season3.pkl','rb') as f:
    sentis3 =pickle.load(f)
    
with open('season4.pkl','rb') as f:
    sentis4 =pickle.load(f)

with open('season5.pkl','rb') as f:
    sentis5 =pickle.load(f)



fig = plt.figure()
ax = fig.add_subplot(111)
sentiments1 = [get_sentiments(senti1) for senti1 in sentis1]
sentiments2 = [get_sentiments(senti2) for senti2 in sentis2]
sentiments3 = [get_sentiments(senti3) for senti3 in sentis3]
sentiments4 = [get_sentiments(senti4) for senti4 in sentis4]
sentiments5 = [get_sentiments(senti5) for senti5 in sentis5]

#positive
Video1pos = [sent['pos'] for sent in sentiments1]
Video2pos = [sent['pos'] for sent in sentiments2]
Video3pos = [sent['pos'] for sent in sentiments3]
Video4pos = [sent['pos'] for sent in sentiments4]
Video5pos = [sent['pos'] for sent in sentiments5]

#neg

Video1neg = [sent['neg'] for sent in sentiments1]
Video2neg = [sent['neg'] for sent in sentiments2]
Video3neg = [sent['neg'] for sent in sentiments3]
Video4neg = [sent['neg'] for sent in sentiments4]
Video5neg = [sent['neg'] for sent in sentiments5]

#neu

Video1neu = [sent['neu'] for sent in sentiments1]
Video2neu = [sent['neu'] for sent in sentiments2]
Video3neu = [sent['neu'] for sent in sentiments3]
Video4neu = [sent['neu'] for sent in sentiments4]
Video5neu = [sent['neu'] for sent in sentiments5]
  
mean_of_postives1=sum(Video1pos)/len(Video1pos)
mean_of_postives2=sum(Video2pos)/len(Video2pos)
mean_of_postives3=sum(Video3pos)/len(Video3pos)
mean_of_postives4=sum(Video4pos)/len(Video4pos)

mean_of_postives5=sum(Video4pos)/len(Video5pos)


mean_of_negatives1=sum(Video1neg)/len(Video1neg)
mean_of_negatives2=sum(Video2neg)/len(Video2neg)
mean_of_negatives3=sum(Video3neg)/len(Video3neg)
mean_of_negatives4=sum(Video4neg)/len(Video4neg)
mean_of_negatives5=sum(Video5neg)/len(Video5neg)

mean_of_neutral1=sum(Video1neu)/len(Video1neu)
mean_of_neutral2=sum(Video2neu)/len(Video2neu)
mean_of_neutral3=sum(Video3neu)/len(Video3neu)
mean_of_neutral4=sum(Video4neu)/len(Video4neu)
mean_of_neutral5=sum(Video5neu)/len(Video5neu)
'''
n=5
index=np.arange(n)
barwidth=0.25
opacity=0.5

Positive=[mean_of_postives1,mean_of_postives2,mean_of_postives3,mean_of_negatives4,mean_of_negatives5]
Negative=[mean_of_negatives1,mean_of_negatives2,mean_of_postives3,mean_of_negatives4,mean_of_negatives5]
Neutral=[mean_of_neutral1,mean_of_neutral2,mean_of_neutral3,mean_of_neutral4,mean_of_neutral5]


objects=('SEASON1','SEASON2','SEASON3','SEASON4','SEASON5')

rects1 = plt.bar(index, Positive, barwidth,
alpha=opacity,
color='g',
label='Positive')

rects2 = plt.bar(index + barwidth, Negative, barwidth,
alpha=opacity,
color='r',
label='Negative')

rects3 = plt.bar(index + barwidth +opacity, Neutral, barwidth,
alpha=opacity,
color='g',
label='Neutral')


plt.xticks(index + barwidth, objects)
plt.ylabel('Mean of Sentiments')
plt.title('Sentiment analysis of Black Mirror show reviews')

'''
objects=('SEASON1','SEASON2','SEASON3','SEASON4','SEASON5')
mean1=sum(rating1)/len(rating1)
mean2=sum(rating2)/len(rating2)
mean3=sum(rating3)/len(rating3)
mean4=sum(rating4)/len(rating4)
mean5=sum(rating5)/len(rating5)
data1=[mean1,mean2,mean3,mean4,mean5]
print(mean1,mean2,mean3,mean4,mean5)
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib import rcParams
import numpy as np
import pandas as pd

plt.plot(objects,data1[0:5],'r.-',marker="P",label='Average Rating')
plt.xticks(rotation=20)
plt.ylabel('Rating')
plt.title('Black mirror movie rating according to its seasons')
plt.legend()
plt.ylim(0,10)
plt.show() 
plt.savefig('mygraph.png',transparent=True)
'''
plt.legend()
plt.tight_layout()

plt.show()
plt.savefig('mygraph.png',transparent=True)
'''