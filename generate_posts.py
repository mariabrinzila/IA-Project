from tkinter import messagebox
import tweepy as tw
from datetime import datetime
from datetime import timedelta


def submit_input(keyword_variable, number_variable):
    keyword = keyword_variable.get()
    number = number_variable.get()
    error = False
    print("The user has chosen the keyword " + str(keyword) +
          ". The user has chosen the number of tweets " + str(number))

    # Troubleshoot for errors (number)
    if number < 10 or number > 500:
        messagebox.showerror("Error:", "Sorry but the number of tweets has "
                                       "to be at least 10 and less than "
                                       "500. Please try again!")
        error = True

    if not error:
        generate_output(keyword, number)
        return number


def generate_output(keyword, number):
    CONSUMER_KEY = 'UUDLYN62cOCW1EGbp8IIFHUD6'
    CONSUMER_SECRET = 'WwbnEVN52kUaYPrNO9cilGq5R7mvErjaFEGBBwcOcFg7T1jb2x'
    OAUTH_TOKEN = '1466436088105422863-uLg18WcVpmuaYfxYN6uyeCso7kSYCc'
    OAUTH_TOKEN_SECRET = 'Q4WjNRVofToBfTcnkVgxciUcXBOAerwZw3mN8ZjiyqQny'

    auth = tw.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tw.API(auth)

    NUMBER_of_TWEETS = 20
    SEARCH_BEHIND_DAYS = 60
    today_date = datetime.today().strftime('%Y-%m-%d')

    today_date_datef = datetime.strptime(today_date, '%Y-%m-%d')
    start_date = today_date_datef - timedelta(days=SEARCH_BEHIND_DAYS)

    tweets = tw.Cursor(api.search_tweets, q=keyword).items(number)

    for tweet in tweets:
        print(tweet.text)
