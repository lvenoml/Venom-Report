import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from Tools import HadoopClient


def RefactorSearchStream(status):   # filters old tweets and gets clean text
    text = None
    if "extended_tweet" in status._json:
        text = status._json["extended_tweet"]["full_text"]
    elif "retweeted_status" in status._json:
        text = status._json["retweeted_status"]["text"]
    else:
      text = status._json["text"]
    clean_text = extractURLs(text)
    f = open("TimeStamp.txt", "w").write(str(status.created_at))
    print(clean_text)


def RefactorSearchResults(search):  # filters old tweets and gets clean text
    clean_results = []
    f = open("TimeStamp.txt", "r").read()
    fresh_results = [tweet for tweet in search if str(tweet.created_at) > str(f)]
    for tweet in fresh_results:
        text = None
        if "retweeted_status" in tweet._json:
            text = (tweet._json["retweeted_status"]["full_text"])
        else:
            text = (tweet._json["full_text"])

        clean_text = extractURLs(text)
        clean_results.append(clean_text)
    f = open("TimeStamp.txt", "w").write(str(search[0].created_at))
    return clean_results

def extractURLs(text):    #Extracts urls and cleans them from text, stores them into external file
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if(len(urls) == 0):
        return text
    else:
        text_withoutUrls = text
        text_URLs = set({})
        '''Real_URLs = set({})  
        #f = open("UrlsForScraper.txt", "a")'''     #Uncoment this if you want to extract urls to external file
        for url in urls:
            text_URLs.add(url)
            text_withoutUrls = text_withoutUrls.replace(url, "")  #replace urls with white space
        '''for url in text_URLs:  #check if urls are accessable
            #try:
                #res = urlopen(url)
                #Real_url = res.geturl()            #Uncoment this if you want to extract urls to external file
                #Real_URLs.add(Real_url)
            #except:
                #print("Invalid url: " + url)
        #for url in Real_URLs:
            #f.write(url + "\n")'''
        return text_withoutUrls

