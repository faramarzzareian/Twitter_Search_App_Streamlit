import tweepy
import pandas as pd
import streamlit as st
import datetime

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a function to search for tweets containing a given keyword in a given Twitter account
def search_tweets(username, keyword):
    tweets = api.user_timeline(screen_name=username, count=100)
    results = []
    for tweet in tweets:
        if keyword.lower() in tweet.text.lower():
            results.append((tweet.text, tweet.favorite_count, tweet.retweet_count, f"https://twitter.com/{username}/status/{tweet.id}"))
    return results

# Set up the Streamlit app
st.title("Twitter Search App")
st.write("Enter one or more Twitter usernames (separated by commas) and a keyword to search for all tweets containing the keyword.")

# Get the user input
usernames = st.text_input("Twitter usernames (separated by commas)")
keyword = st.text_input("Keyword")

# Perform the search when the user clicks the button
if st.button("Search"):
    if not usernames:
        st.error("Please enter at least one Twitter username.")
    elif not keyword:
        st.error("Please enter a keyword to search for.")
    else:
        usernames_list = [u.strip() for u in usernames.split(",")]
        for username in usernames_list:
            results = search_tweets(username, keyword)
            st.write(f"Results for {username} and keyword '{keyword}':")
            if results:
                for i, (tweet, likes, retweets, link) in enumerate(results):
                    st.write(f"Likes: {likes} | Retweets: {retweets}")
                    st.write(tweet)
                    st.write(link)
                    if i < len(results) - 1:
                        st.write("---")
                    if i == 1:  # Show only two tweets for each account
                        break
            else:
                st.write("No results found for this user.")
            st.write("")