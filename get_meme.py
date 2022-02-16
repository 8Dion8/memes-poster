import praw
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("id")
client_secret = os.getenv("secret")
password = os.getenv("accpass")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="User-Agent: script:memes-grabber:v0.0.1 (by /u/GameOfShadows)",
    username="GameOfShadows",
    password=password
)

SUBREDDIT = "dankmemes"

subreddit = reddit.subreddit(SUBREDDIT)
hot = subreddit.hot(limit=10)

pattern = re.compile("http.*i\.redd\.it\/.*\.(gif|png|jpg)")

for post in hot:
    post_url = post.url
    if re.search(pattern, post_url):
        print(post.title, "\n            ", post_url)
        img_data = requests.get(post_url).content
        img_name = post_url[18:]
        with open(img_name, "wb") as f:
            f.write(img_data)

