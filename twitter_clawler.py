#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import text_extractor


#Twitter API credentials
consumer_key = "hckXV3mSh0nTurJYfVJkLqYcQ"
consumer_secret = "YTJo6WNODgxDmSiHKDCUSZEphQ3lgUwjM8L97Wsf3mHXigCaM5"
access_key = "1128323858350661634-hoo9xE30fKZSpNXypWsXXffe4qCjsT"
access_secret = "7lfEc1oaAXfelGn8hYtlYJ8HUp3vEMM5mHG7oYJc9xFvD"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    num = 10
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=num)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=num,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 100):#set total tweets grabed here.
            break
        print("...%s tweets downloaded so far" % len(alltweets))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print("Done")
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@realDonaldTrump")
    text_extractor.text_extractor()