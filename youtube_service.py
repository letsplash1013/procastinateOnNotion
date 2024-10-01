import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")

def fetch_top_youtube_videos():
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={YOUTUBE_CHANNEL_ID}&part=snippet,id&order=date&maxResults=5"
    response = requests.get(url)
    data = response.json()
    
    videos = []
    for item in data.get("items", []):
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        videos.append({
            "title": video_title,
            "url": video_url,
            "source": "YouTube"
        })
    
    return videos
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetch_youtube_videos(channel_id, limit=5):
    """Fetch the latest videos from a specified YouTube channel."""
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=limit,
        order="date"
    )
    response = request.execute()
    
    video_data = []
    for item in response['items']:
        video_data.append({
            "title": item['snippet']['title'],
            "url": f"https://www
