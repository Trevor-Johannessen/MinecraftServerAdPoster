import praw
import json

f = open('submission.json')
submission = json.load(f)

f = open('settings.json')
settings = json.load(f)

reddit = praw.Reddit(
    client_id=settings['client_id'],
    client_secret=settings['client_secret'],
    user_agent=settings['user_agent'],
    username=settings['username'],
    password=settings['password']
)

subreddit = reddit.subreddit('powerstests')



if submission['flair'] == "":
    subreddit.submit(title=submission['title'], selftext=submission['body'])
else:
    flairs = {}
    try:
        # Get all subreddit flairs
        for flair in subreddit.flair.link_templates.user_selectable():
            flairs[flair.flair_text] = flair.flair_template_id
        print(flairs)
    except:
        # Subreddit has no flairs
        subreddit.submit(title=submission['title'], selftext=submission['body'])
        pass

    subreddit.submit(title=submission['title'], flair_id=flairs[submission['flair']], selftext=submission['body'])