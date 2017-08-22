import praw
import OAuth2Util
import urllib.request
from credentials import reddit

subreddit = reddit.subreddit('dankmemes')


for submission in subreddit.hot(limit=100) :
    link=submission.url
    title=submission.title
    title=title.replace(" ","_")
    title=title.replace("/","-")
    title="".join(["downloads/",title,".jpg"])
    urllib.request.urlretrieve(link,title)