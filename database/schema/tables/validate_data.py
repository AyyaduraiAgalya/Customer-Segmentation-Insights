from db_connect import get_connection


def validate_customers():
    """
    Validates the data in the customers table.
    """
    query = "SELECT * FROM customers.customers;"
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        print("\nCustomers Table Data:")
        for row in rows:
            print(row)

    # Check uniqueness of CustomerID
    query = """
    SELECT CustomerID, COUNT(*)
    FROM customers.customers
    GROUP BY CustomerID
    HAVING COUNT(*) > 1;
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        duplicates = cur.fetchall()
        if duplicates:
            print("\nDuplicate CustomerIDs found:")
            for row in duplicates:
                print(row)
        else:
            print("\nAll CustomerIDs are unique.")


def validate_products():
    """
    Validates the data in the products table.
    """
    query = "SELECT * FROM products.products;"
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        print("\nProducts Table Data:")
        for row in rows:
            print(row)

    # Check uniqueness of ProductCategory
    query = """
    SELECT ProductCategory, COUNT(*)
    FROM products.products
    GROUP BY ProductCategory
    HAVING COUNT(*) > 1;
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        duplicates = cur.fetchall()
        if duplicates:
            print("\nDuplicate ProductCategories found:")
            for row in duplicates:
                print(row)
        else:
            print("\nAll ProductCategories are unique.")


def validate_transactions():
    """
    Validates the data in the transactions table and checks relationships.
    """
    query = """
    SELECT t.TransactionID, c.CustomerID, c.Gender, p.ProductCategory, t.Quantity, t.TotalAmount
    FROM transactions.transactions t
    INNER JOIN customers.customers c ON t.CustomerID = c.CustomerID
    INNER JOIN products.products p ON t.ProductID = p.ProductID;
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        print("\nTransactions and Relationships Data:")
        for row in rows:
            print(row)

    # Validate TotalAmount calculation
    query = """
    SELECT TransactionID, Quantity, Price, TotalAmount,
           (Quantity * Price) AS CalculatedAmount
    FROM transactions.transactions t
    JOIN products.products p ON t.ProductID = p.ProductID
    WHERE TotalAmount != (Quantity * Price);
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        mismatches = cur.fetchall()
        if mismatches:
            print("\nMismatches in TotalAmount calculation:")
            for row in mismatches:
                print(row)
        else:
            print("\nAll TotalAmount values are correctly calculated.")


def validate_relationships():
    """
    Validates foreign key relationships between tables.
    """
    query = """
    SELECT t.TransactionID, t.CustomerID, t.ProductID
    FROM transactions.transactions t
    LEFT JOIN customers.customers c ON t.CustomerID = c.CustomerID
    LEFT JOIN products.products p ON t.ProductID = p.ProductID
    WHERE c.CustomerID IS NULL OR p.ProductID IS NULL;
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        invalid_references = cur.fetchall()
        if invalid_references:
            print("\nInvalid foreign key references in transactions:")
            for row in invalid_references:
                print(row)
        else:
            print("\nAll foreign key references are valid.")


if __name__ == "__main__":
    print("Validating Sample Data...")

    print("\n=== Validating Customers Table ===")
    validate_customers()

    print("\n=== Validating Products Table ===")
    validate_products()

    print("\n=== Validating Transactions Table ===")
    validate_transactions()

    print("\n=== Validating Relationships ===")
    validate_relationships()

    print("\nValidation Complete.")
