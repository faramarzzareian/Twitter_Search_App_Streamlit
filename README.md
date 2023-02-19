# Twitter Search App

This is a Python script for a Streamlit app that searches for tweets containing a given keyword in one or more Twitter accounts.
# Getting Started

To use this app, you will need to have a Twitter developer account and obtain API credentials. You can create a new developer account or manage your existing account here.

Once you have your API credentials, you can update the consumer_key, consumer_secret, access_token, and access_token_secret variables at the beginning of the script.
# Installation

To run this app, you will need to have Python 3 installed on your system. You can download the latest version of Python from the official website.

After installing Python, you can install the required packages by running the following command in your terminal:

        pip install tweepy pandas streamlit

# Usage

To run the app, navigate to the directory containing the script in your terminal and run the following command:

       streamlit run app.py

This will start the Streamlit app, and you should be able to access it in your web browser at:
       http://localhost:8501/.

To use the app, enter one or more Twitter usernames (separated by commas) and a keyword to search for all tweets containing the keyword. Click the "Search" button to perform the search.

The app will display the tweet text, number of likes, number of retweets, and link for each result. It will show only two tweets for each Twitter account that matches the search query.
