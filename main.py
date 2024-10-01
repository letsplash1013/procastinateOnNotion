from reddit_service import fetch_top_reddit_posts
from notion_service import add_post_to_notion

def main():
    subreddit_name = "all"  # Can change it to a list of subreddits
    limit = 5  # Number top posts
    
    top_posts = fetch_top_reddit_posts(subreddit_name, limit)
    
    for post in top_posts:
        add_post_to_notion(post)

if __name__ == "__main__":
    main()
