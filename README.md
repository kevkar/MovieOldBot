# MovieOldBot

This is a Twitter bot that posts tweets that make you feel old. [Check it out here](https://twitter.com/KevinKarch2)

![Alt text](https://i.imgur.com/ZVVRNd8.png)

# Set-up Instructions

The first thing you need to do is apply for a developer account on Twitter to get access to their API.
This is a very simple process and can be done here: https://developer.twitter.com/en/apply-for-access

There are two outside libraries that you'll need to install: tweepy and pandas.
You can do this through Pycharm through File->Settings->Project:<project-name>->Project Interpreter
  Click on the plus on the right and search for the libraries. 
  
  ![Alt text](https://i.imgur.com/x3rpITT.png)
  
  You can also just do pip install tweepy and pip install pandas in your prefered shell.
  
  If your Twitter developer account was approved (it was instantaneous for me), log in and click on "Keys and tokens"
You should see four different keys.
The only difference between the code here and the code on my PC is on lines 9-13. Where I've put consumer_key, consumer_secret,
key, and secret, replace those with your API key, API secret key, Access token, and Access token secret, respectively. This will connect the program to your twitter account. 

  ![Alt text](https://i.imgur.com/7WRHMVw.png)
  
# How It Works

The program uses pandas' retrieval of data from csv files and converts it to a hashmap (dictionary). The file MoviesList.csv is in the form of title:year and 
EventsList.cvs is in the form of year:event. 

![Alt text](https://i.imgur.com/uTDOG0n.png)

The program gets a random movie from the movies list and finds an event from the year that is one year closer to the movie than it is to today. For example, Batman (1989) is 31 years from 2020. The event value for key 1969 (30 years before 1989) is "beginning of the Vietnam War". 

When you start the program, you should see "Authentication Success" and then the prompt "Type y to generate new tweet, t to tweet, q to quit"
If you don't like the first tweet it generates, try a new one. You could also directly change the csv files if you don't like some of the events or movies. 

![Alt text](https://i.imgur.com/DwrZt2E.png)

The movies are mostly from the IMDB top 250 with a few taken out and few added to fill in the years that didn't have a movie. You can add as many movies as you want but make sure there is only one event per year!
