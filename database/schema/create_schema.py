from db_connect import get_connection

# Defining schema configurations
SCHEMA_CONFIG = {
    "sales": "Schema for all sales and transaction-related data.",
    "customers": "Schema for customer demographic and profile information.",
    "products": "Schema for product catalog and inventory data.",
}

def create_schema(schema_name, description):
    """
    Creates a single schema in the PostgreSQL database.
    Skips creation if the schema already exists.
    """
    query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"Schema '{schema_name}' created or already exists. Description: {description}")

def create_all_schemas():
    """
    Iterates through SCHEMA_CONFIG and creates all defined schemas.
    """
    for schema, desc in SCHEMA_CONFIG.items():
        create_schema(schema, desc)

if __name__ == "__main__":
    print("Starting schema creation...")
    create_all_schemas()
    print("Schema creation complete.")
