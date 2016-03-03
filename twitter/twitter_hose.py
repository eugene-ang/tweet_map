#Import the necessary methods from tweepy library
#import requests
from elasticsearch import Elasticsearch
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "703045938764455938-IOECMv6mInP9acthhxcr949HeZpk68S"
access_token_secret = "8NbUvf37X4cSnl7cQO4ujU9SRKagriz3254Bf9l7q1kK3"
consumer_key = "9lD6HkCUF6TGEqSXrKFNQ1ZPk"
consumer_secret = "NtJHp4W3bTickJvdfJU5eOvoHEY4Yx6p2MymEqTQlj0kYevklu"
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


class ElasticSearchStreamListener(StreamListener):
    'This class is a stream-listener that redirects the stream to be stored in ElasticSearch'
    def on_data(self, data):
        try:
            # I need to get this done in another process, or just read the geo field
            #jsondata = json.loads(data)
            #if jsondata['geo'] != None:
            #    print(jsondata['geo'])
            if data.find('"geo":') != -1 & data.find('"geo":null') == -1:

                # Parse json
                jsondata = json.loads(data)
                print(jsondata['geo'])

                # Build own dictionary with subset of the data
                d = {}
                d['text'] = jsondata['text']
                d['name'] = jsondata['user']['name']
                d['created_at'] = jsondata['created_at']
                lat_degdec = jsondata['geo']['coordinates'][0]
                lon_degdec = jsondata['geo']['coordinates'][1]
                coordict = {}
                coordict['lat'] = float(lat_degdec)
                coordict['lon'] = float(lon_degdec)
                d['location'] = coordict

                # Encode as json
                processed = json.dumps(d)

                # Send to back-end for storage
                es.index(index="tweets", doc_type='tweet', body=processed)
                
        except KeyboardInterrupt:
            print("Interrupted by Ctrl-C.")
            raise KeyboardInterrupt
        return True

    def on_error(self, status):
        print ("Reached on_error() for ElasticSearchStreamListener.")
        print ("status: ", status)
        #if status_code == 420:
        #    return False
        

if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = ElasticSearchStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['bluenote', 'villagevanguard', 'smalls'])
    #stream.sample()

    i = 0
    keepGoing = True
    while keepGoing:
        try:
            i = i + 1
            print ('Streaming... ' + str(i))
            # Get tweets from every corner of the world
            stream.filter(locations=[-180,-90,180,90])
            #stream.sample()
        except KeyboardInterrupt:
            #print ('Interrupted by Ctrl-C.')
            keepGoing = False
        except Exception as e:
            print ('Caught exception...')
            print ( e )
            continue
    

def authAndGetStream(self):
    l = StdOutListener()
    # TODO: should read these secrets from a config file
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    return stream

def streamTwitter(self, stream):
    #stream.filter(parameter=value)
    stream.filter(locations=[-180,-90,180,90])

def streamTwitter(self, stream, trackparams):
    stream.filter(track=trackparams)
    
