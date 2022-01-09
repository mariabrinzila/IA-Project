import tweepy as tw
from datetime import datetime
from datetime import timedelta
     
CONSUMER_KEY ='UUDLYN62cOCW1EGbp8IIFHUD6'
CONSUMER_SECRET ='WwbnEVN52kUaYPrNO9cilGq5R7mvErjaFEGBBwcOcFg7T1jb2x'
OAUTH_TOKEN = '1466436088105422863-uLg18WcVpmuaYfxYN6uyeCso7kSYCc'
OAUTH_TOKEN_SECRET = 'Q4WjNRVofToBfTcnkVgxciUcXBOAerwZw3mN8ZjiyqQny'

# auth = tw.OAuthHandler(API_KEY, API_SECRET)
# auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
# api = tw.API(auth, wait_on_rate_limit=True)
# api.update_status('tweepy + oauth!')

auth = tw.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tw.API(auth)

 
NUMBER_of_TWEETS = 20
SEARCH_BEHIND_DAYS=60
today_date=datetime.today().strftime('%Y-%m-%d')
 
 
today_date_datef = datetime.strptime(today_date, '%Y-%m-%d')
start_date = today_date_datef - timedelta(days=SEARCH_BEHIND_DAYS)
 
keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input ("Please enter how many tweets to analyze: "))
tweets = tw.Cursor(api.search_tweets, q=keyword).items(noOfTweet)

for tweet in tweets:
  print(tweet.text)