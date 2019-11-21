from textblob import TextBlob
import datetime
from textblob.exceptions import NotTranslated
import collections
import tweepy 
import json
import requests

from constantes_globales import *


class TwitterUser():
    def __init__(self,screen_name,limit_tweets):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)
        self.screen_name=screen_name
        self.limit_tweets=limit_tweets
        self.user=""
        self.tweets=[]
    def autenticarUsuario(self):
        result=""
        try:
            self.user = self.api.get_user(self.screen_name)
            result=True
        except:
            result=False
        finally:
            return result
    
    def strip_undesired_chars(self,tweet):
        stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
        char_list = [stripped_tweet[j] for j in range(len(stripped_tweet)) if ord(stripped_tweet[j]) in range(89654)]
        stripped_tweet=''
        for j in char_list:
            stripped_tweet=stripped_tweet+j
        return stripped_tweet
    
    def fetch_tweets(self):
        alltweets=self.api.user_timeline(screen_name = self.screen_name,count=self.limit_tweets)
        self.tweets = [ [tweet.created_at,self.strip_undesired_chars(tweet.text)] for tweet in alltweets] 
    def getStadistics(self):
        self.fetch_tweets()
        frecuencyDict=self.getTweetsGroupByMonths()
        return self.getAVGPolaritiesSubjectivities(frecuencyDict)
    def getAVGPolaritiesSubjectivities(self,frecuencias):
        estadisticas={}
        for key in frecuencias.keys():
            totalPolaridades=0
            totalSubjectividades=0
            for date,tweet in self.tweets:
                if months[date.month]==key:
                    polaridad,subjectividad=self.getSentiment(tweet)
                    totalPolaridades+=polaridad
                    totalSubjectividades+=subjectividad
            averagePolaridades=totalPolaridades/frecuencias[key]
            averageSubjectividades=totalSubjectividades/frecuencias[key]
            estadisticas.update({key:{"polaridad":averagePolaridades,"subjectividad":averageSubjectividades}})
        return estadisticas

    def getTweetsGroupByMonths(self):
        tweetsPerMonth=[]
        for date,text in self.tweets:
            tweetsPerMonth.append(months[date.month])
        frecuencyPerMonth=collections.Counter(tweetsPerMonth)
        return frecuencyPerMonth
    
    def getSentiment(self,tweet):
        analisis= TextBlob(tweet)
        translated=analisis
        try:
            translated=analisis.translate(from_lang='es', to='en')
        except NotTranslated:
            pass
        return translated.sentiment.polarity,translated.sentiment.subjectivity
   

if __name__ == '__main__':
    user=TwitterUser("malditaternura",200)
    user.autenticarUsuario()
    print(user.getTweetsGroupByMonths())
    print(user.getStadistics())
    


