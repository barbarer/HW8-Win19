# -*- coding: utf-8 -*-
# SI 206
# Homework 8 - Twitter Data and Caching
# Note: Read Homework 8 spec for detailed instructions.

import unittest
import tweepy
import requests
import json

## **** Be sure to have twitter_info.py that contains your
## consumer_key, consumer_secret, access_token, and access_token_secret,
## in the same directory as this file.  Do NOT add and commit
## that file to your Github repo
import twitter_info

## Get your secret values to authenticate to Twitter.
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and
# return it in a JSON-formatted way
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def read_cache(cache_file):
    """
    This function reads from the JSON cache file and returns a dictionary from the cache data. 
    If the file doesn’t exist, it returns an empty dictionary.  You might need to open the file
    for reading with encoding="utf-8"
    Note: see cache_example.py for example code.  
    """

    pass

def write_cache(cache_file, cache_dict):
    """
    This function writes the dictionary into a JSON file to save the cached dictionary
    """
    dumped_json_cache = json.dumps(cache_dict) # serialize dictionary to a JSON formatted string 
    fw = open(cache_file,"w") # open the cache file
    fw.write(dumped_json_cache) # write the JSON
    fw.close() # Close the open file


def get_tweet_data_with_caching(cache_file, search_term):
    """
    This function searches for the search term in the dictionary returned by read_cache.
    If the search term exists in the dictionary, it should print 'using cache' and 
    return the results for that search term. If the search term does not exist
    in the dictionary, the function should make a call to the twitter API to get the search
    results and print "fetching".  If there were results, it should add them to the dictionary 
    and write out the dictionary to a file using write_cache. If there was an exception 
    during the search, it should print out a message and return None.
    """
    pass

    

def print_tweets(cache_file):
    """
    This function loops 3 times and each time it asks for a search term from the user.
    Then, it gets the results of the search term using get_tweet_data_with_caching.
    If there were at least 5 tweets it prints out the tweet text and created_at values 
    from the first 5 tweets with a blank line after each as shown in the sample output. 
    Otherwise it prints "Found x tweets" where x is the number of tweets found.
    """
    
    pass
        

### Extra Credit ###
def get_most_common_search_term(cache_file):
    """
    This function returns a list of tuples, where each tuple contains the search term 
    and the number of tweets for that search term in the dictionary from the cached file, 
    in descending order from most tweets to least tweets.

    For the orginal cache_twitter.json it should return:
    [('Hope', 15), ('Thanksgiving', 14), ('Space', 12), ('horse', 11), ('Trump', 10), ('Halloween', 9)]
    """
    


class TestTwitterAPI(unittest.TestCase):
    def setUp(self):
        self.cache = 'cache_twitter.json'
        
    def test_read_cache(self):
        self.assertTrue("Thanksgiving" in read_cache(self.cache).keys())
        self.assertIsInstance(read_cache(self.cache), dict)
    
    def test_get_cached_data(self):
        self.assertEqual(get_tweet_data_with_caching(self.cache, "Thanksgiving")["statuses"][0]["user"]["name"], "ad0rey")
        self.assertEqual(get_tweet_data_with_caching(self.cache, "Space")["statuses"][1]["entities"]["user_mentions"][0]["screen_name"], "therattlespace")
        

# This calls the above test cases
if __name__ == "__main__":
    # Unit test only tests your read_cache and get_tweet_data_with_caching functions with certain test cases.
    # For this HW, you should look at the grading rubric to understand how your code will be tested by the 
    # grading team.

    unittest.main(verbosity=2)
    
    # The code below calls get_most_common_search_term and prints the result
    # Uncomment below when you are trying Extra-credit
    #print(get_most_common_search_term("cache_twitter.json"))

    #uncomment the code below to test print_tweets live and to fetch new data
    #print_tweets("cache_twitter.json")

   
