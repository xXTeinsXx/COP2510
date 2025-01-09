import sqlite3

def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Sql statements
    sql = '''CREATE TABLE Inventory(
    Item ID INTEGER PRIMARY KEY NOT NULL,
    ItemName TEXT,
    Price REAL)'''

    sql = '''INSERT INTO Inventory(Item ID, ItemName,Price)
    VALUES (1, "Paint Brush", 8.99)'''

    cur.execute(sql)
    cur.execute('''INSERT INTO Inventory(
    Item ID, ItemName,Price)
    VALUES (1, "Paint Brush", 8.99)''')
    results= cur.fetchall()

    for row in results:
        print(f'{row[0]:30} {row[1]:5}')
    
    conn.commit()
    conn.close()

main()