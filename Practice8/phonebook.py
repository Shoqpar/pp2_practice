import csv
from connect import get_db_connection
from pathlib import Path


def setup_database():
    base_dir = Path(__file__).resolve().parent

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL UNIQUE
                );
            """)

            with open(base_dir / "functions.sql", "r", encoding="utf-8") as f:
                cur.execute(f.read())

            with open(base_dir / "procedures.sql", "r", encoding="utf-8") as f:
                cur.execute(f.read())

            conn.commit()


def import_contacts_from_csv(file_path):
    names = []
    phones = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 2:
                name, phone = row
                names.append(name.strip())
                phones.append(phone.strip())

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
            conn.commit()


def get_all_contacts():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, phone FROM contacts ORDER BY id;")
            return cur.fetchall()


def search_contacts(pattern):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
            return cur.fetchall()


def get_contacts_paginated(limit, offset):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
            return cur.fetchall()


def upsert_contact(name, phone):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
            conn.commit()


def delete_contact(value):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact_by_value(%s);", (value,))
            conn.commit()


def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return

    for row in rows:
        print(row)


if __name__ == "__main__":
    setup_database()

    while True:
        print("\nPhoneBook Menu")
        print("1. Show all contacts")
        print("2. Search contacts by pattern")
        print("3. Add or update contact")
        print("4. Import contacts from CSV")
        print("5. Show contacts with pagination")
        print("6. Delete by name or phone")
        print("7. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            print_contacts(get_all_contacts())

        elif choice == "2":
            pattern = input("Enter pattern: ").strip()
            print_contacts(search_contacts(pattern))

        elif choice == "3":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            upsert_contact(name, phone)
            print("Contact inserted/updated.")

        elif choice == "4":
            file_path = input("Enter CSV file path: ").strip()
            import_contacts_from_csv(file_path)
            print("CSV import completed.")

        elif choice == "5":
            limit = int(input("Enter LIMIT: ").strip())
            offset = int(input("Enter OFFSET: ").strip())
            print_contacts(get_contacts_paginated(limit, offset))

        elif choice == "6":
            value = input("Enter name or phone to delete: ").strip()
            delete_contact(value)
            print("Contact deleted if it existed.")

        elif choice == "7":
            print("Bye!")
            break

        else:
            print("Invalid choice.")