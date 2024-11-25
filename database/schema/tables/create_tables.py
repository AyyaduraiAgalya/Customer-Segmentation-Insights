from db_connect import get_connection

def create_tables():
    """
    Creates all necessary tables in their respective schemas.
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
        """,

        # Customers Table
        """
        CREATE TABLE IF NOT EXISTS customers.customers (
            CustomerID VARCHAR(50) PRIMARY KEY,
            Gender VARCHAR(10) NOT NULL,
            Age INT CHECK (Age > 0 OR Age IS NULL),
            Region VARCHAR(50)
        );
        """,
        # Products Table
        """
        CREATE TABLE IF NOT EXISTS products.products (
            ProductID SERIAL PRIMARY KEY,
            ProductCategory VARCHAR(50) NOT NULL UNIQUE, -- Added UNIQUE constraint
            Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0)
        );
        """,
        # Transactions Table
        """
        CREATE TABLE IF NOT EXISTS transactions.transactions (
            TransactionID VARCHAR(50) PRIMARY KEY,
            Date DATE NOT NULL,
            CustomerID VARCHAR(50) NOT NULL,
            ProductID INT NOT NULL,
            Quantity INT NOT NULL CHECK (Quantity >= 0),
            TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),
            FOREIGN KEY (CustomerID) REFERENCES customers.customers(CustomerID),
            FOREIGN KEY (ProductID) REFERENCES products.products(ProductID)
        );
        """
    ]

    with get_connection() as conn:
        cur = conn.cursor()
        for query in queries:
            cur.execute(query)
        conn.commit()
        print("All tables created successfully in their respective schemas!")

if __name__ == "__main__":
    print("Starting table creation...")
    create_tables()
    print("Table creation complete.")
