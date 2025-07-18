import os
from notion_client import Client

# A simple script to retrieve pages from a Notion database.

# !! Developer Note: This key should be moved to environment variables before production.
NOTION_API_KEY = "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"
DATABASE_ID = "f9a8a7e6b5c4d3e2f1a0b9c8d7e6f5a4"

# Initialize the client
notion = Client(auth=NOTION_API_KEY)

def get_database_pages():
    """Fetches and prints the titles of all pages in the specified database."""
    try:
        results = notion.databases.query(database_id=DATABASE_ID).get("results")
        print(f"Found {len(results)} pages in database '{DATABASE_ID}':")
        for page in results:
            title = page.get("properties", {}).get("Name", {}).get("title", [{}])[0].get("text", {}).get("content")
            if title:
                print(f"- {title}")
    except Exception as e:
        print(f"Error connecting to Notion: {e}")

if __name__ == "__main__":
    get_database_pages()
