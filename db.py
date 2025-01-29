import asyncio
import asyncpg
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print("DEBUG: Supabase DB URL:", os.getenv("SUPABASE_DB_URL"))

# Get Supabase Database URL
DB_URL = os.getenv("SUPABASE_DB_URL")

async def fetch_data(query, params=None):
    """Connects to Supabase PostgreSQL and runs a SELECT query."""
    conn = None
    try:
        if not DB_URL:
            raise ValueError("❌ Database URL is missing! Check your .env file.")

        print(f"🔗 Connecting to database: {DB_URL}")  # Debugging Line

        # Establish database connection
        conn = await asyncpg.connect(DB_URL)
        print("✅ Connected to Supabase Database")

        # Execute query
        rows = await conn.fetch(query, *params) if params else await conn.fetch(query)

        # Convert results to list of dictionaries
        results = [dict(row) for row in rows]
        return results

    except Exception as e:
        print(f"❌ Database Connection Error: {str(e)}")  # Detailed Error Message
        return None

    finally:
        if conn:
            await conn.close()
            print("🔄 Connection closed")

# Example usage
async def main():
    query = "SELECT * FROM all_data LIMIT 10;"  # Replace with your actual table
    data = await fetch_data(query)
    
    if data is None:
        print("❌ Query failed. Check your database connection and query syntax.")
    else:
        print("✅ Query Results:", data)

# Run async function
if __name__ == "__main__":
    asyncio.run(main())
