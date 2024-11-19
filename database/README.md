
# PostgreSQL Database Setup for Customer Segmentation Project

This README provides step-by-step instructions to set up the PostgreSQL database for the Customer Segmentation Project. By following this guide, you will connect to a PostgreSQL database, create the necessary schemas, and verify their existence using pgAdmin on macOS.

---

## Prerequisites

1. **macOS** system.
2. **PostgreSQL** installed. Follow [PostgreSQL macOS Installation Guide](https://www.postgresql.org/download/macosx/) if not installed.
3. **pgAdmin** installed for database visualization.
4. **Python 3.8 or above** installed with the following libraries:
    - `psycopg2`
    - `dotenv`

Install Python libraries via pip:
```bash
pip install psycopg2-binary python-dotenv
```

---

## Steps to Set Up the Database

### 1. Install PostgreSQL
1. Download and install PostgreSQL from the [official website](https://www.postgresql.org/download/macosx/).
2. Start the PostgreSQL service using:
    ```bash
    brew services start postgresql
    ```

3. Confirm the installation by opening the PostgreSQL interactive terminal:
    ```bash
    psql --version
    ```

### 2. Create a New Database
1. Open the PostgreSQL terminal (`psql`) or pgAdmin and run the following command to create a new database:
    ```sql
    CREATE DATABASE customersegmentation;
    ```

2. Verify the database creation:
    ```sql
    \l
    ```

### 3. Configure Database Connection
1. Clone the repository or create a directory for your project:
    ```bash
    git clone https://github.com/{{your-username}}/Customer-Segmentation-Insights.git
    cd Customer-Segmentation-Insights
    ```
Replace {{your-username}} with your github username.

2. Create a `.env` file in the project directory to securely store database credentials:
    ```bash
    touch .env
    ```

3. Add the following variables to the `.env` file:
    ```
    DB_NAME=customersegmentation
    DB_USER=<your_postgresql_user>
    DB_PASSWORD=<your_postgresql_password>
    DB_HOST=localhost
    DB_PORT=5432
    ```

### 4. Verify Database Connection
1. Use the `db_connect.py` script provided in the repository to test the connection:
    ```python
    import psycopg2
    from contextlib import contextmanager
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv()

    @contextmanager
    def get_connection():
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
    ```

2. Run the script:
    ```bash
    python db_connect.py
    ```

   If the connection is successful, you will see:
   ```
   Database connection successful!
   ```

### 5. Create Database Schemas
1. Use the `create_schema.py` script to define and create schemas for organizing your data. Below is the script for schema creation:
    ```python
    from db_connect import get_connection

    SCHEMA_CONFIG = {
        "sales": "Schema for all sales and transaction-related data.",
        "customers": "Schema for customer demographic and profile information.",
        "products": "Schema for product catalog and inventory data.",
    }

    def create_schema(schema_name, description):
        query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            print(f"Schema '{schema_name}' created or already exists. Description: {description}")

    def create_all_schemas():
        for schema, desc in SCHEMA_CONFIG.items():
            create_schema(schema, desc)

    if __name__ == "__main__":
        print("Starting schema creation...")
        create_all_schemas()
        print("Schema creation complete.")
    ```

2. Run the script to create schemas:
    ```bash
    python create_schema.py
    ```

3. Verify schemas in pgAdmin:
    - Open `pgAdmin` and connect to the `retail_analysis` database.
    - Expand the `Schemas` node to confirm the creation of `sales`, `customers`, and `products` schemas.

---

## Next Steps
With the database schema in place, wee will proceed to load the dataset and begin the analysis. I'll update this README as the project progresses.

---

**Author:** AGALYA AYYADURAI  
**License:** MIT
