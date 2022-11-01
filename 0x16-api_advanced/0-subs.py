#!/usr/bin/python3

'''-Write a function that queries the
`[Reddit API](https://www.reddit.com/dev/api/)` and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
-Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re setting
 a custom User-Agent.

Requirements:
    -Prototype: `def number_of_subscribers(subreddit)`
    -If not a valid subreddit, return 0.
    -NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
'''

import requests

headers = {'user-agent': 'Reddit Scraper'}


def number_of_subscribers(subreddit):
    """Returns number of subscribers of a subreddit"""
    about_endpoint = 'https://www.reddit.com/r/{}/about.json'
    url = about_endpoint.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        about = response.json()
        return about.get("data").get("subscribers")
    if response.status_code == 404 or response.status_code == 302:
        return 0
