import tweepy 
import json
import requests 
consumer_key = "JpSTg1k14QaRqzI4yGe1W9YFC"
consumer_secret = "Xph4zxuCuBMLSZ5bVUSCx5O0LyK6x4OaaLez1vjtZJYhTfOz3y"
access_key = "1196658811509059584-hqsaleqDvD899XW81rSE9CkZQu5bTk"
access_secret = "5gTTkpNcVGRtpXW8Xv348JkJPQ0o8qzNrTGeHCZqpVv2Z"

def strip_undesired_chars(tweet):
    stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
    char_list = [stripped_tweet[j] for j in range(len(stripped_tweet)) if ord(stripped_tweet[j]) in range(89654)]
    stripped_tweet=''
    for j in char_list:
        stripped_tweet=stripped_tweet+j
    return stripped_tweet

def get_all_tweets(screen_name):
    limit_number = 3240
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    user = api.get_user(screen_name)
    print(user.__dict__)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    outtweets = [(tweet.id_str, tweet.created_at, strip_undesired_chars(tweet.text),tweet.retweet_count,str(tweet.favorite_count)+'') for tweet in alltweets]
    justText = [(strip_undesired_chars(tweet.text)) for tweet in alltweets]   
    #print(justText)


usuario = input("Ingrese el nombre de usuario a analizar: ")
get_all_tweets(usuario)


