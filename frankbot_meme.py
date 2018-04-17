import praw
import random
from passwords import REDDIT_ID, REDDIT_PASS, REDDIT_USER, REDDIT_SECRET

filetypes = ("jpg", "png", "gif") #getting img posts only
def meme(msg=None):
    #create the reddit instance
    reddit = praw.Reddit(client_id=REDDIT_ID,
                         client_secret=REDDIT_SECRET,
                         user_agent='my user agent',
                         username=REDDIT_USER,
                         password=REDDIT_PASS)
    images = []
    if msg is None: #if no sub is specified, pick a random one from the list
        sub = "all"
    else:
        sub = msg #or pass the subreddit parameter to the value
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        if submission.url.endswith(filetypes):
            images.append([submission.url, submission.title])
    return images[random.randint(0, len(images) - 1)]
