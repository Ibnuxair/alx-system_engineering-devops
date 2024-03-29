#!/usr/bin/python3
"""
A recursive function that queries the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            if not children:
                # No more articles, return the collected titles
                return hot_list

            # Extract titles and append to the hot_list
            titles = [post['data'].get(
                'title') for post in children if post['data'].get('title')]
            hot_list.extend(titles)

            # Recursive call for the next page
            next_after = data.get('after')
            if next_after is not None:
                return recurse(subreddit, hot_list, next_after)
            else:
                return hot_list

        else:
            return None

    except requests.exceptions.RequestException as e:
        return None
