#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the num

of subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid API request issues
    headers = {"User-Agent": "MyRedditApp/1.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            # Parse JSON response and extract the number of subscribers
            subreddit_data = response.json().get("data")
            subscribers_count = subreddit_data.get("subscribers")
            return subscribers_count if subscribers_count is not None else 0

        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
