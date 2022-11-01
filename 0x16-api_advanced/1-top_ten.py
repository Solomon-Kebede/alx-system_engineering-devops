#!/usr/bin/python3

'''-Write a function that queries the
`[Reddit API](https://www.reddit.com/dev/api/)` and prints the titles of
the first 10 hot posts listed for a given subreddit.

Requirements:
    -Prototype: `def top_ten(subreddit)`
    -If not a valid subreddit, print None.
    -NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
'''


import requests
headers = {'user-agent': 'Reddit Scraper'}


def top_ten(subreddit):
    """Returns top ten results for a subreddit"""
    top_endpoint = 'https://www.reddit.com/r/{}/top.json'
    url = top_endpoint.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        top = response.json()
        top25 = top.get("data").get("children")
        count = 0
        for result in top25:
            if count == 10:
                break
            count += 1
            print(result.get("data").get("title"))
    if response.status_code == 404 or response.status_code == 302:
        print(None)
