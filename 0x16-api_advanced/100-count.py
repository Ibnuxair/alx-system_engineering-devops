#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all

hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Count occurrences of given keywords in the titles"""
    if count_dict is None:
        count_dict = {}

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
                # No more articles, print the sorted count
                print_sorted_count(count_dict)
                return

            # Extract titles and count occurrences of keywords
            for post in children:
                title = post['data'].get('title', '').lower()
                count_occurrences(title, word_list, count_dict)

            # Recursive call for the next page
            next_after = data.get('after')
            if next_after is not None:
                count_words(subreddit, word_list, next_after, count_dict)
            else:
                print_sorted_count(count_dict)
        else:
            return None

    except requests.exceptions.RequestException as e:
        return None


def count_occurrences(title, word_list, count_dict):
    """
    Count occurrences of keywords in a title and update the count dictionary.
    """
    for word in word_list:
        count = title.count(word.lower())
        count_dict[word] = count_dict.get(word, 0) + count


def print_sorted_count(count_dict):
    """
    Print the sorted count of occurrences for each keyword.
    """
    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_count:
        print(f"{word.lower()}: {count}")
