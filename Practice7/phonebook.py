import csv
import os
from connect import get_db_connection

def create_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) UNIQUE NOT NULL
                );
            """)
            conn.commit()

def import_from_csv(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, file_name)
    
    contacts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f: #
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                contacts.append((row[0], row[1]))
        
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    contacts
                )
                conn.commit()
                print(f"Импортировано записей: {len(contacts)}")
    except FileNotFoundError:
        print("Файл contacts.csv не найден!")

def add_contact(name, phone):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s);", (name, phone))
            conn.commit()

def update_contact(target_name, new_phone):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s;", (new_phone, target_name))
            conn.commit()
            print(f"Обновлено строк: {cur.rowcount}")

def query_contacts(filter_type, value):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            if filter_type == 'name':
                cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (value + '%',))
            elif filter_type == 'phone':
                cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s;", (value + '%',))
            
            for row in cur.fetchall():
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

def delete_contact(identifier):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s;", (identifier, identifier))
            conn.commit()
            print(f"Удалено записей: {cur.rowcount}")

def display_all_contacts():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, phone FROM phonebook ORDER BY id;")
            
            rows = cur.fetchall()
            
            if not rows:
                print("\nPhonebook is empty.")
                return

            print("\n--- list of all contacts ---")
            print(f"{'ID':<5} | {'Name':<15} | {'Tel':<15}")
            print("-" * 40)
            
            for row in rows:
                print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<15}")

if __name__ == "__main__":
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Import CSV | 2. Show all contacts | 3. Add Contact | 4. Update | 5. Search | 6. Delete | 7. Exit")
        choice = input("Select: ")

        if choice == '1':
            import_from_csv('contacts.csv')
        elif choice == '2':
            display_all_contacts()
        elif choice == '3':
            add_contact(input("Name: "), input("Phone: "))
        elif choice == '4':
            update_contact(input("Target Name: "), input("New Phone: "))
        elif choice == '5':
            print("Search by: 1. Name 2. Phone Prefix")
            sub = input("Choice: ")
            val = input("Value: ")
            query_contacts('name' if sub == '1' else 'phone', val)
        elif choice == '6':
            delete_contact(input("Name or Phone to delete: "))
        elif choice == '7':
            break