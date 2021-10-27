
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "isDxz34F0XzLsZqPENtKQES69"
csecret = "ZkedbyovIk36XYvCh1Vf2QhjanZzFpRJvoLp8puj56qe8OIPmn"
atoken = "115946548-4gCGrDFsmddR8nSSohG40950E2GtmqVpWOnXTP8y"
asecret = "TzooW4w4pCXVRPzliyW4jbt8V9oBVNrHgkrAJjodvv5t6"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('juegos2021')
except:
    db = server['juegos2021']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[11.4037,41.7901,13.9414,43.568])  
twitterStream.filter(track=['fortnite','freefire'])
