import tweepy
from time import sleep

consumer_key="Z5dDoNOB1efZTIHsc3K39BTFa"
consumer_secret="0OmTmSNH7whf7V06Z4LE3W4zXDAwxPKk9d948RLlQCBv7NgMyG"
access_token="746388158-iY84sri3WGMULG9Hw3Q00ICurtA3pm8IMAho1gq7"
access_token_secret="H6oTFv58fmrkmaluiNTuBKxgpRnFK08hgtMH5c79u6ZEG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorising your access, login
auth.set_access_token(access_token, access_token_secret) #set access token
auth.secure = True #make it secure = yes
api = tweepy.API(auth) #allows us to use the API

#print(str(api.get_user(screen_name = '@eliakah'))) # to chek if the screenname match and verify that we logged in

##Let's begin the bot


#this just fetches the most recent entries for #
for tweet in tweepy.Cursor(api.search,q='#rowanuniversity', lang='en').items():
    try:
        print("Found tweet by: @"+ tweet.user.screen_name)
        print("Found tweet by user_id: "+ str(tweet.user.id))
        print("User Location: "+ str(tweet.user.location))
        print("Saying: '" + tweet.text+"'")

        ids = []
        for page in tweepy.Cursor(api.followers_ids, screen_name=tweet.user.screen_name).pages():
            ids.extend(page)

        print("User has "+ str(len(ids)) + " followers \n")

    except tweepy.TweepError as e:
        print (e.reason)
        sleep(10)
        continue
    except StopIteration:
        break
