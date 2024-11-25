from db_connect import get_connection

def migrate_tables():
    """
    Applies schema changes to existing tables.
    """

    queries = [
        # Modifying Age column to allow NULL values
        """
        ALTER TABLE customers.customers 
        ALTER COLUMN Age DROP NOT NULL,
        ADD CONSTRAINT Age_check CHECK (Age > 0 OR Age IS NULL);
        """
    ]

    with get_connection() as conn:
        cur = conn.cursor()
        for query in queries:
            cur.execute(query)
        conn.commit()
        print("Migration applied successfully!")

if __name__ == "__main__":
    print("Starting migration...")
    migrate_tables()
    print("Migration complete.")
