from db_connect import get_connection


def rename_schema(old_name, new_name):
    """
    Renames a schema in PostgreSQL securely.
    """
    query = f"ALTER SCHEMA {old_name} RENAME TO {new_name};"

    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute(query)
            conn.commit()
            print(f"Schema '{old_name}' successfully renamed to '{new_name}'!")
        except Exception as e:
            conn.rollback()
            print(f"Error renaming schema '{old_name}' to '{new_name}': {e}")


if __name__ == "__main__":
    old_name = input("Enter the current schema name: ")
    new_name = input("Enter the new schema name: ")
    rename_schema(old_name, new_name)
