#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the num of subscribers.
"""

import requests


def subreddit_exists(subreddit):
    """Check if subreddit exist."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Check if the status code is 200
        return response.status_code == 200

    except requests.exceptions.RequestException as e:
        # An exception occurred, indicating an issue with the request
        return False


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit."""
    # Check if the subreddit exists before making the actual API call
    if not subreddit_exists(subreddit):
        return 0

    # Continue with the original function
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            # Parse JSON response and extract the number of subscribers
            subreddit_data = response.json().get("data")
            subscribers_count = subreddit_data.get("subscribers", 0)
            return subscribers_count

        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
