#DO THIS LATER
#this is the same as the tutorial http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#want to modify this to include geo info but not done/ working yet

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = '20501555-eyk6NDluk1Q6Bcw8mbfgPdtoS9Z7bFFUbzeE0McGg'
access_token_secret = 'khRxFmpau2t0s2YQnUPCPcjFAbyZ3b00cW3bhGQT7VEPr'
consumer_key = 'Ch5OQyULKt4GrvLdqeSAMztdv'
consumer_secret = 'nuQyvsXWYQFSvzXMjhmUhcYFtkniVvM99lysZJX1M00sME58nc'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #original, saving #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['weather', 'wind', 'snow'])

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['trump','theresa may','clinton'])
