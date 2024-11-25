from db_connect import get_connection

def insert_sample_data():
    """
    Inserts sample data into the database tables for validation purposes.
    """
    queries = [
        # Insert sample products
        """
        INSERT INTO products.products (ProductCategory, Price)
        VALUES 
            ('Electronics', 500.00),
            ('Clothing', 50.00),
            ('Groceries', 20.00),
            ('Furniture', 250.00)
        ON CONFLICT (ProductCategory) DO NOTHING;
        """,
        
        # Insert sample customers
        """
        INSERT INTO customers.customers (CustomerID, Gender, Age, Region)
        VALUES 
            ('C001', 'Male', NULL, 'North'),
            ('C002', 'Female', 30, 'East'),
            ('C003', 'Male', 35, 'South'),
            ('C004', 'Female', 28, 'West')
        ON CONFLICT (CustomerID) DO NOTHING;
        """,

        # Insert sample transactions
        """
        INSERT INTO transactions.transactions (TransactionID, Date, CustomerID, ProductID, Quantity, TotalAmount)
        VALUES 
            ('T001', '2024-01-01', 'C001', 1, 1, 500.00),
            ('T002', '2024-01-02', 'C002', 2, 3, 150.00),
            ('T003', '2024-01-03', 'C001', 3, 10, 200.00),
            ('T004', '2024-01-04', 'C003', 4, 2, 500.00)
        ON CONFLICT (TransactionID) DO NOTHING;
        """
    ]

    with get_connection() as conn:
        cur = conn.cursor()
        for query in queries:
            cur.execute(query)
        conn.commit()
        print("Sample data inserted successfully!")

if __name__ == "__main__":
    print("Inserting sample data...")
    insert_sample_data()
    print("Sample data insertion complete.")