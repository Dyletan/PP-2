import psycopg2

# "CREATE TABLE phonebook (Userid SERIAL PRIMARY KEY, Username varchar(255) NOT NULL, Phone varchar(255) NOT NULL);"

def add_user(cur):
    # a = input("Do you want to add a user?\nPress 'Y' if you want and 'N' otherwise\n")
    while True:
        a = input("Do you want to add a user?\nPress 'Y' if you want and 'N' otherwise\n")
        if a.lower() == "y":
            b = 'y'
            while b.lower() == 'y':
                username = input("Input the username: ")
                phone = input("Input the phone number: ")
                cur.execute(f"INSERT INTO phonebook (Username,Phone) VALUES ('{username}', '{phone}');")
                b =  input("Do you want to add another user?\nIf so, write 'Y' and anything else otherwise\n")
            break
        elif a.lower() == "n":
            print("Okay, not adding users")
            break

def change_username(userid, username, cur):
    cur.execute(f"UPDATE phonebook SET Username = {username} WHERE Userid = {userid}")

def change_phone(userid, phone, cur):
    cur.execute(f"UPDATE phonebook SET Phone = {phone} WHERE Userid = {userid}")

def users_by_ascending(cur):
    cur.execute("SELECT Username, Phone FROM phonebook ORDER BY Username")
    rows = cur.fetchall()
    for row in rows:
        print(f"User: {row[0]}  Phone: {row[1]}")

def search_by_id(cur, userid):
    cur.execute(f"SELECT Useranme, Phone FROM phonebook WHERE Userid = {userid};")
    result = cur.fetchone()
    print(f"User: {result[0]}  Phone: {result[1]}")

def search_by_username(cur, username):
    cur.execute(f"SELECT Userid, Phone FROM phonebook WHERE Username = {username};")
    result = cur.fetchone()
    print(f"User id: {result[0]}  Phone: {result[1]}")

def search_by_phone(cur, phone):
    cur.execute(f"SELECT Userid, Username FROM phonebook WHERE Phone = {phone};")
    result = cur.fetchone()
    print(f"User id: {result[0]}  Username: {result[1]}")

def delete_by_userid(cur, userid):
    cur.execute(f"DELETE FROM phonebook WHERE Userid = {userid};")

def delete_by_username(cur, username):
    cur.execute(f"DELETE FROM phonebook WHERE Username = {username};")

def load_csv(cur, path):
    with open(path, 'r') as file:
        next(file) # Skip the header row.
        cur.copy_from(file, 'phonebook', sep=',')


conn = None
try:
    conn = psycopg2.connect(
    host="localhost",
    database="pp2",
    user="postgres",
    password="pass")
    
    # create a cursor
    cur = conn.cursor()

    # add_user(cur)

    # for i in [6,7,8]:
    #     delete_by_userid(cur, i)

    load_csv(cur, r"C:\PP 2\lab_10\phonenums.csv")

    users_by_ascending(cur)

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')

