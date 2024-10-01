from notion_client import Client
from datetime import datetime
from config import NOTION_TOKEN, NOTION_DATABASE_ID

notion = Client(auth=NOTION_TOKEN)

def add_post_to_notion(post):
    """Adds a Reddit post to a Notion database."""
    notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties={
            "Name": {"title": [{"text": {"content": post["title"]}}]},
            "URL": {"url": post["url"]},
            "Score": {"number": post["score"]},
            "Subreddit": {"rich_text": [{"text": {"content": post["subreddit"]}}]},
            "Created": {"date": {"start": datetime.utcfromtimestamp(post["created_utc"]).isoformat()}},
        }
    )
    print(f"Added post '{post['title']}' to Notion.")
