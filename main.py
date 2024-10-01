from config import TWITTER_USERNAME, YOUTUBE_CHANNEL_ID
from reddit_service import fetch_top_reddit_posts
from notion_service import add_post_to_notion, add_tweet_to_notion, add_youtube_video_to_notion
from twitter_service import fetch_tweets
from youtube_service import fetch_youtube_videos

def main(subreddit_name="all", limit=5):
    # Fetch Reddit posts
    top_posts = fetch_top_reddit_posts(subreddit_name, limit)
    for post in top_posts:
        add_post_to_notion(post)
    
    # Fetch Tweets
    tweets = fetch_tweets(TWITTER_USERNAME, limit)
    for tweet in tweets:
        add_tweet_to_notion(tweet)
    
    # Fetch YouTube Videos
    videos = fetch_youtube_videos(YOUTUBE_CHANNEL_ID, limit)
    for video in videos:
        add_youtube_video_to_notion(video)

if __name__ == "__main__":
    main()
