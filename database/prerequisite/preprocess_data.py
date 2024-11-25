import pandas as pd


def preprocess_data(file_path):
    """
    Cleans and preprocesses the Kaggle dataset for database insertion.

    Parameters:
    file_path (str): Path to the Kaggle dataset CSV file.

    Returns:
    dict: Preprocessed dataframes for customers, products, and transactions.
    """
    # Loading the dataset
    print("Loading dataset...")
    data = pd.read_csv(file_path)

    # Renaming columns to match the database schema
    print("Renaming columns to match database schema...")
    data.rename(columns={'Customer_ID': 'CustomerID',
                         'Product_Category': 'ProductCategory',
                         'Amount': 'Price',
                         'Transaction_ID': 'TransactionID',
                         'Total_Purchases': 'Quantity',
                         'Total_Amount': 'TotalAmount',
                         'City': 'Region'}, inplace=True)

    # Handling missing values
    print("Handling missing values...")
    data.fillna({
        'CustomerID': 'Unknown',
        'Gender': 'Unknown',
        'Region': 'Unknown',
        'ProductCategory': 'Unknown',
        'Quantity': 0,
        'Price': 0.0,
        'TotalAmount': 0.0
    }, inplace=True)

    # Removing duplicates
    print("Removing duplicates...")
    data.drop_duplicates(inplace=True)

    # Replacing Age values greater than 120 with None (NULL in PostgreSQL)
    print("Processing Age column...")
    data['Age'] = data['Age'].apply(lambda x: None if x > 120 else x)

    # Converting Age column to integer (float values will be replaced with NaN first)
    data['Age'] = data['Age'].astype('Int64')  # Use 'Int64' to handle nullable integers

    print(data['CustomerID'].dtype)
    # Converting CustomerID to string
    data['CustomerID'] = data['CustomerID'].astype(str)
    print(data['CustomerID'].dtype)

    print(f"Max Age: {data['Age'].max()}, Min Age: {data['Age'].min()}")
    print(data['Age'].dtype)

    # Replacing NA values with None for postgres compatibility
    data = data.where(pd.notnull(data), None)

    # Creating the customers table
    print("Creating customers table...")
    customers = data[['CustomerID', 'Gender', 'Age', 'Region']].drop_duplicates()

    # Creating the products table
    print("Creating products table...")
    products = data[['ProductCategory', 'Price']].drop_duplicates()

    # Creating the transactions table
    print("Creating transactions table...")
    transactions = data[['TransactionID', 'Date', 'CustomerID', 'ProductCategory', 'Quantity', 'TotalAmount']]

    print("Data preprocessing complete!")
    return {
        'customers': customers,
        'products': products,
        'transactions': transactions
    }


if __name__ == "__main__":
    file_path = "data/raw/retail_data.csv"

    print("Starting preprocessing...")
    preprocessed_data = preprocess_data(file_path)

    # Saving preprocessed data to parquetœ
    preprocessed_data['customers'].to_parquet("data/preprocessed/customers.parquet", index=False)
    preprocessed_data['products'].to_parquet("data/preprocessed/products.parquet", index=False)
    preprocessed_data['transactions'].to_parquet("data/preprocessed/transactions.parquet", index=False)

    print("Preprocessed data saved as parquet files!")
