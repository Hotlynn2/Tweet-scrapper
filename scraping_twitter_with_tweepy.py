import credentials as c
import tweepy 

# setting up tweepy authorization 

auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
auth.set_access_token(c.access_token,c.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# scraping tweets from a text search query

text_query = 'nanaado'+'lockdown'

tweets = tweepy.Cursor(api.search, q=text_query, lang='en').items(10)

for tweet in tweets:
    print(tweet.created_at,tweet.text,tweet.source,tweet.user.name)