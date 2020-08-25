import tweepy
import datetime
import pandas
import random


# creates API with four keys from twitter development kit
def createAPI():
    auth = tweepy.OAuthHandler("Js5BOHpIl2VLKIAE5QxT7tXLj",
                               "ABTWy3taPtEaPFJaOoOiygty8vS8tHXB1du4p6ASYJcSwCB3Jk")
    auth.set_access_token("1297879170463207425-3WWnEosU3tggNxzzpaMgfdGWGzB6uc",
                          "I8RyGSxGQqrBmytOFeCWD0LhemsSn9HOtQ2DdbDYQi4mX")

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authentication Success")
    except:
        print("Failure Authenticating")

    return api


api = createAPI()

# creates dict of col1:col2 key:value
def getCSV(csv, col1, col2):
    df = pandas.read_csv(csv, usecols=[col1, col2])
    return df.set_index(col1)[col2].to_dict()


# creates the movie and event dictts from csv files
movieDict = getCSV('MoviesList.csv', 'title', 'year')
eventDict = getCSV('EventsList.csv', 'year', 'event')
print(movieDict)
print(eventDict)


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
    return random.choice(list(movieDict.keys()))


# tweets out stuff
def tweet(api,tweet):
    api.update_status(tweet)


def doProgram(api,movieDict,eventDict):
    while True:
        print("Type y to generate new tweet, t to tweet, q to quit")
        x = input()
        if x == 'y':
            randomMovie = randomMovieTitle(movieDict)
            theTweet = getTweet(randomMovie, movieDict, eventDict)
            print(theTweet)
        elif x == 't':
            tweet(api, theTweet)
            break
        elif x == 'q':
            break


doProgram(api, movieDict, eventDict)
