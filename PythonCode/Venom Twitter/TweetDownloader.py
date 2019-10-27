from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import sys
from Tools import TwitterCredentials as TC, TextPocessing

auth = OAuthHandler(TC.consumer_key, TC.consumer_secret)
auth.set_access_token(TC.access_key, TC.access_secret)
api = tweepy.API(auth)
tags = ["Venom", "Marvel"]


class TwitterAPI:

    def InitiateStream(self):   # will begin the twitter stream
        listener = StdOutListener()
        stream = Stream(auth, listener)
        stream.filter(track=tags)
        print("/////////////////////////////////////\n")
        print("Stream Started...\n")
        print("/////////////////////////////////////\n")

    def Search(self):   #will pull last n(specified) messeges from searbox timeline
        print("/////////////////////////////////////\n")
        print("Beginning to download the timeline...\n")
        print("/////////////////////////////////////\n")
        search_results = api.search(q=str(tags), count=100, lang = "en", tweet_mode='extended')
        clean_search = set(TextPocessing.RefactorSearchResults(search_results))
        TextPocessing.PrepeareForDataTransfer(list(clean_search))
        print("/////////////////////////////////////\n")
        print("downloading finished, beginning the stream...\n")
        print("/////////////////////////////////////\n")
        self.InitiateStream()


class StdOutListener(StreamListener):   # Twitter API methods

    def on_status(self, status):    #This executes when a message is pulled from a stream
        print("message received: created at " + str(status.created_at))
        clean_text = TextPocessing.RefactorSearchStream(status)
        TextPocessing.PrepeareForDataTransfer(clean_text)
        return



    def on_error(self, status_code,):   #If something bad happens
        if status_code == 420:
            print("The limit was exeeded")
        else:
            print(status_code)
        sys.exit(0)

if(__name__ == "__main__"): #START PROGRAM
    print("Here we go \n")
    Twitter = TwitterAPI()
    Twitter.Search()


















