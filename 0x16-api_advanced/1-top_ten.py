#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid API request issues
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        params = {'limit': 10}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        if response.status_code == 200:
            # Parse JSON response and extract post titles
            data = response.json().get('data', {})
            children = data.get('children', [])

            for post in children:
                title = post['data'].get('title')
                if title:
                    print(title)
                else:
                    print("Title not found for a post.")
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
        return None
