# procastinateOnNotion Setup Guide

1. **Clone the Repo**: Download the project from your GitHub repository.

2. **Install Dependencies**: Use `requirements.txt` to install all necessary Python packages.

3. **Create Reddit App**:
   - Go to [Reddit Apps](https://www.reddit.com/prefs/apps) and create a new app.
   - Choose "Script" as the type.
   - Save the **Client ID**, **Client Secret**, and create a **User Agent**.

4. **Create Notion Integration**:
   - Go to [Notion Integrations](https://www.notion.so/my-integrations) and create a new integration.
   - Copy the **Internal Integration Token**.

5. **Create Notion Database**:
   - In Notion, create a database with columns for "Name", "URL", "Score", "Subreddit", and "Created".
   - Share the database with the integration.
   - Copy the **Database ID** from the URL.

6. **Set Up Environment Variables**:
   - Create a `.env` file in your project with the following variables:

     ```
     REDDIT_CLIENT_ID=your_reddit_client_id
     REDDIT_CLIENT_SECRET=your_reddit_client_secret
     REDDIT_USER_AGENT=your_reddit_user_agent
     NOTION_TOKEN=your_notion_integration_token
     NOTION_DATABASE_ID=your_notion_database_id
     ```

7. **Run the Program**: Execute `main.py` to fetch Reddit posts and add them to your Notion database.
