#!/usr/bin/python3
"""Contains a function that prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            children = data.get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print('None')
    except requests.exceptions.RequestException:
        print('None')
