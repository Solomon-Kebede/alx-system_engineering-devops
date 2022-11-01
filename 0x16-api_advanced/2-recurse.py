#!/usr/bin/python3

'''-Write a recursive function that queries the
`[Reddit API](https://www.reddit.com/dev/api/)` and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.

-Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
    -Prototype: `def recurse(subreddit, hot_list=[])`
    -Note: You may change the prototype, but it must be able to be called
    with just a subreddit supplied. AKA you can add a counter, but it must
    work without supplying a starting value in the main.
    -If not a valid subreddit, return None.
    -NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
-Your code will NOT pass if you are using a loop and not recursively calling
the function! This /can/ be done with a loop but the point is to use a
recursive function. :)
'''

import requests
headers = {'user-agent': 'Reddit Scraper'}


def recurse(subreddit, hot_list=[], after=None, count=None):
    """Recurses and returns a list containing the titles
    of all hot articles for a given subreddit"""
    if after is None and count is None:
        after = ''
        count = 0

    hot_endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'

    url = hot_endpoint.format(subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot = response.json()
        children = hot.get("data").get("children")
        after = hot.get("data").get("after")
        for child in children:
            title = child.get("data").get("title")
            hot_list.append(title)
        if len(hot_list) < 1:
            return None
        while True:
            if after is not None:
                recurse(subreddit, hot_list, after, count)
                break
            if after is None:
                break
        return hot_list
    if response.status_code == 404 or response.status_code == 302:
        return None
