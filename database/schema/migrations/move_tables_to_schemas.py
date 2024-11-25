from db_connect import get_connection

def move_tables_to_schemas():
    """
    Moves tables from the public schema to their respective custom schemas.
    """
    commands = [
        "ALTER TABLE public.customers SET SCHEMA customers;",
        "ALTER TABLE public.products SET SCHEMA products;",
        "ALTER TABLE public.transactions SET SCHEMA transactions;"
    ]

    with get_connection() as conn:
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        print("Tables moved to their respective schemas successfully!")

if __name__ == "__main__":
    print("Moving tables to schemas...")
    move_tables_to_schemas()
    print("Table migration complete.")
