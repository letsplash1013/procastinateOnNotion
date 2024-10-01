import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_top_reddit_posts(subreddit_name, limit=5):
    """Fetch top Reddit posts of the day from a specified subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top("day", limit=limit)
    
    posts = []
    for post in top_posts:
        posts.append({
            "title": post.title,
            "url": post.url,
            "score": post.score,
            "subreddit": post.subreddit.display_name,
            "created_utc": post.created_utc
        })
    
    return posts
