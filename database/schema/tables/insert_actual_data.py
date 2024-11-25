import pandas as pd
from db_connect import get_connection


def load_data():
    # Loading the preprocessed data
    customers = pd.read_parquet("data/preprocessed/customers.parquet")
    products = pd.read_parquet("data/preprocessed/products.parquet")
    transactions = pd.read_parquet("data/preprocessed/transactions.parquet")

    print(customers['Age'].max())
    print(customers['Age'].min())
    print(customers['Age'].isnull().sum())

    # Replacing null values in Date to 1900-01-01 so it doesnt violates the NOT NULL constraint
    transactions['Date'] = transactions['Date'].fillna('1900-01-01')

    # Replacing other NA values with None for postgres compatibility
    customers = customers.where(pd.notnull(customers), None)
    products = products.where(pd.notnull(products), None)
    transactions = transactions.where(pd.notnull(transactions), None)
    customers['Age'] = customers['Age'].replace({pd.NA: None})


    with get_connection() as conn:
        cur = conn.cursor()

        # Inserting Customers
        for _, row in customers.iterrows():
            query = """
            INSERT INTO customers.customers (CustomerID, Gender, Age)
            VALUES (%s, %s, %s)
            ON CONFLICT (CustomerID) DO NOTHING;
            """
            cur.execute(query, (row['CustomerID'], row['Gender'], row['Age']))

        # Inserting Products
        for _, row in products.iterrows():
            query = """
            INSERT INTO products.products (ProductCategory, Price)
            VALUES (%s, %s)
            ON CONFLICT (ProductCategory) DO NOTHING;
            """
            cur.execute(query, (row['ProductCategory'], row['Price']))

        # Inserting Transactions
        for _, row in transactions.iterrows():
            query = """
            INSERT INTO transactions.transactions (TransactionID, Date, CustomerID, ProductID, Quantity, TotalAmount)
            VALUES (%s, %s, %s, 
                    (SELECT ProductID FROM products.products WHERE ProductCategory = %s), 
                    %s, %s)
            ON CONFLICT (TransactionID) DO NOTHING;
            """
            cur.execute(query, (
            row['TransactionID'], row['Date'], row['CustomerID'], row['ProductCategory'], row['Quantity'],
            row['TotalAmount']))

        conn.commit()
        print("Data inserted successfully!")


if __name__ == "__main__":
    load_data()
