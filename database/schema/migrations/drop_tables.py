from db_connect import get_connection

def drop_tables():
    """
    Applies schema changes to existing tables.
    """

    queries = [
        # Dropping the transactions table
        """
        DROP TABLE IF EXISTS transactions.transactions;
        """,

        # Dropping the products table
        """
        DROP TABLE IF EXISTS products.products;
        """,

        # Dropping the customers table
        """
        DROP TABLE IF EXISTS customers.customers;
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
    drop_tables()
    print("Migration complete.")



