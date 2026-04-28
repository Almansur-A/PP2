import csv
from connect import conn, cur

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

def insert_from_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )
    conn.commit()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()

def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()

def query_contacts():
    filter_name = input("Enter name filter (or press Enter): ")
    if filter_name:
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + filter_name + '%',))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_contact():
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()

while True:
    print("\n1.Insert CSV\n2.Insert Console\n3.Update\n4.Query\n5.Delete\n6.Exit")
    choice = input("Choose: ")

    if choice == "1":
        insert_from_csv()
    elif choice == "2":
        insert_from_console()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        query_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break

cur.close()
conn.close()