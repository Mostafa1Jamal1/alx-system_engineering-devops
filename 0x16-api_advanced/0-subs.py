#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given, the function should return 0.'''
import requests
from uuid import uuid4


def number_of_subscribers(subreddit):
    ''' for a given subreddit returns the number of subscribers '''
    headers = {'user-agent': 'Mozilla/5.0 AppleWebKit/537.36 holberton school'}
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
