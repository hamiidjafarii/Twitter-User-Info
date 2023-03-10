import pandas as pd
import configparser
import tweepy



excel_file_path = 'tweets.xlsx'
sheet_name = 'Tweets'

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = config['twitter']['CONSUMER_SECRET']
ACCESS_KEY = config['twitter']['ACCESS_KEY']
ACCESS_SECRET = config['twitter']['ACCESS_SECRET']


def twitter_OAuth(consumer_key,consumer_secret,access_key,access_secret):
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api = tweepy.API(auth)
    return api

api = twitter_OAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

user_name = []
excel_data_df = pd.read_excel(excel_file_path, sheet_name = sheet_name)

un = excel_data_df['User Name'].to_list()

for x in un:
    user_name.append(x)
    user_name = list(dict.fromkeys(user_name))


column = ['Id','User Name','Name','Bio','Following','Followers','Verified','Protected','Joined','Location', 'URL']
data = []
tweepy_errors_NotFound = []


for x in user_name:
    try:
        user = api.get_user(screen_name = x)
    except tweepy.errors.NotFound:
        tweepy_errors_NotFound.append(x)
    data.append([user.id, x, user.name ,user.description, user.friends_count, user.followers_count, user.verified,user.protected, user.created_at, user.location, user.url])
    df = pd.DataFrame(data, columns = column)
    df = df.sort_values(by = ['Joined'])
    df.to_csv('data.csv', index = False, encoding='utf-8-sig')

print(len(tweepy_errors_NotFound),'user/users has/have not been found by Tweepy. The list:',tweepy_errors_NotFound)
