import praw
import os
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

