
# Setup Guide

1. **Clone the Repo**  
   Download the project from your GitHub repository.

2. **Install Dependencies**  
   Use the `requirements.txt` to install the necessary Python packages.

3. **Create API Credentials**

   - **Reddit**:  
     Go to [Reddit Apps](https://www.reddit.com/prefs/apps) and create a new app (choose "script" type).  
     Save the **Client ID**, **Client Secret**, and create a **User Agent**.

   - **Twitter**:  
     Create a Twitter developer account at [Twitter Developer Portal](https://developer.twitter.com/).  
     Generate the **Bearer Token**.

   - **YouTube**:  
     Go to [Google Developer Console](https://console.developers.google.com/) and create a project with YouTube Data API enabled.  
     Get the **API Key**.

   - **Notion**:  
     Go to [Notion Integrations](https://www.notion.so/my-integrations) and create an integration.  
     Copy the **Integration Token**.  
     Create a Notion database with fields: `Name`, `URL`, `Score`, `Subreddit`, `Created`.  
     Share the database with the integration and copy the **Database ID** from the URL.

4. **Edit the `.env` File**  
   In the root folder of your project, edit the `.env` file with the following:

   ```
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=your_reddit_user_agent

   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   YOUTUBE_API_KEY=your_youtube_api_key

   NOTION_TOKEN=your_notion_integration_token
   NOTION_DATABASE_ID=your_notion_database_id
   ```

5. **Run the Program**

   - **Option 1: Use Command-Line Arguments**:  
     You can pass dynamic values when running the script:
     ```
     python main.py --subreddit all --twitter elonmusk --youtube UC_x5XG1OV2P6uZZ5FSM9Ttw --limit 5
     ```

   - **Option 2: Use Interactive Input**:  
     Run the program without arguments and it will prompt for inputs:
     ```
     python main.py
     ```

   The program will fetch Reddit posts, Tweets, and YouTube videos and add them to your Notion database.

6. **Optional**: Modify Fetch Limit  
   You can adjust the number of items to fetch by changing the `limit` parameter in the command or when prompted.
