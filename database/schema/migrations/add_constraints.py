from db_connect import get_connection

def add_constraints():
    """
    Adds missing constraints to the existing database tables.
    """
    queries = [
        # Adding UNIQUE constraint to ProductCategory
        """
        ALTER TABLE products.products
        ADD CONSTRAINT products_category_unique UNIQUE (ProductCategory);
        """
    ]

    with get_connection() as conn:
        cur = conn.cursor()
        for query in queries:
            cur.execute(query)
        conn.commit()
        print("Constraints added successfully!")

if __name__ == "__main__":
    print("Adding constraints...")
    add_constraints()
    print("Constraint addition complete.")
