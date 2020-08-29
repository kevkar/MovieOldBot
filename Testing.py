import tweepy
import datetime
import pandas
import random


# creates API with four keys from twitter development kit
def createAPI():
    auth = tweepy.OAuthHandler(consumerkey,
                               secretkey)
    auth.set_access_token(key,
                          secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authentication Success!")
    except:
        print("Authentication Failed!")

    return api


#api object created with above method
api = createAPI()


# creates dict of col1:col2 key:value
def getCSV(csv, col1, col2):
    df = pandas.read_csv(csv, usecols=[col1, col2])
    return df.set_index(col1)[col2].to_dict()


# creates the movie and event dicts from csv files
movieDict = getCSV('MoviesList.csv', 'title', 'year')
eventDict = getCSV('EventsList.csv', 'year', 'event')


# string text of tweet
def getTweet(movieName, movieDict, eventDict):
    thisYear = datetime.datetime.now().year
    movieYear = movieDict[movieName]
    eventYear = movieYear - (thisYear - movieYear - 1)
    return 'The movie ' + movieName + ' (' + str(movieYear) + ')' + \
           ' is closer in time to the ' + eventDict[eventYear] + \
           ' (' + str(eventYear) + ')' + " than it is to today."


# returns random movie title as string
def randomMovieTitle(movieDict):
    movieKeys = list(movieDict.keys())
    return random.choice(movieKeys)


# does the actual tweeting with the twitter api
def tweet(api,tweet):
    api.update_status(tweet)


# if you dont like the random movie, get another one and tweet it
def doProgram(api,movieDict,eventDict,randomMovie):
    while True:
        print("Type n to generate new tweet, t to tweet, q to quit")
        x = input()
        if x == 'n':
            randomMovie = randomMovieTitle(movieDict)
            theTweet = getTweet(randomMovie, movieDict, eventDict)
            print(theTweet)
        elif x == 't':
            if randomMovie == '':
                print("You have to generate a tweet first!")
                continue
            tweet(api, theTweet)
            print("Tweet successful")
            break
        elif x == 'q':
            break
        else:
            print("Invalid command!")


randomMovie = ''
doProgram(api, movieDict, eventDict, randomMovie)

