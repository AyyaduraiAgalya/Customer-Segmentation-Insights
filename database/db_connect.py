import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

@contextmanager
def get_connection():
    """
    Creates a connection to the PostgreSQL database.
    Manages connection lifecycle to ensure proper cleanup.
    """
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
    try:
        yield conn
    finally:
        conn.close()

if __name__ == "__main__":
    with get_connection() as conn:
        print("Database connection successful!")