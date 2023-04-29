import psycopg2

# "CREATE TABLE phonebook (Userid SERIAL PRIMARY KEY, Username varchar(255) NOT NULL, Phone varchar(255) NOT NULL);"
# point number 1
def sort_by_pattern(cur):
    cur.execute("SELECT Username FROM phonebook WHERE Phone LIKE '8747%' OR phone LIKE '+7747%';")
    results = cur.fetchall()
    print("Users that have tele2:")
    for result in results:
        print(result[0])

# point number 2
def check_correctness(phone):
    return (phone[:2] == '87' and len(phone) == 11) or (phone[:3] == "+77" and len(phone) == 12)

def add_or_update(cur):
    username = input("Enter the username: ")
    cur.execute(f"SELECT Userid FROM phonebook WHERE Username = '{username}'")
    result = cur.fetchone()
    if result:
        phone = input("User already exists, update the phone: ")
        while not check_correctness(phone):
            phone = input("Incorrect phone, try again: ")
        cur.execute(f"UPDATE phonebook SET Phone = '{phone}' WHERE Username = '{username}'")
    else:
        phone = input("Input the phone number: ")
        while not check_correctness(phone):
            phone = input("Incorrect phone, try again: ")
        cur.execute(f"INSERT INTO phonebook (username, phone) VALUES ('{username}', '{phone}')")
    
# point number 3
def add_list(cur, list):
    incorrect = []
    for item in list:
        if check_correctness(item[1]):
            cur.execute(f"INSERT INTO phonebook (username, phone) VALUES ('{item[0]}', '{item[1]}')")
        else:
            incorrect.append(item)
    return incorrect

ls = [('Adam', '87125678943'), ('Eve', '12345678901'), ('Zhansulu', '+77894039512'), ('Imanzhan', '88148346432')]

# point number 4
def get_paginated_data(cur, page_num, page_size):
    offset = (page_num - 1) * page_size
    limit = page_size

    cur.execute(f"SELECT * FROM phonebook ORDER BY userid OFFSET {offset} LIMIT {limit}")
    
    rows = cur.fetchall()
    for row in rows:
        print("User id: " + str(row[0]) + ", Username: " + row[1] + ", Phone: " + row[2])

# point number 5
def delete_by_userid(cur, userid):
    cur.execute(f"DELETE FROM phonebook WHERE Userid = {userid};")

def delete_by_username(cur, username):
    cur.execute(f"DELETE FROM phonebook WHERE Username = {username};")

def delete_by_phone(cur, phone):
    cur.execute(f"DELETE FROM phonebook WHERE Phone = {phone};")


# previous lab
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

    # load_csv(cur, r"C:\PP 2\lab_11\phonenums.csv")


    # incorrect = add_list(cur, ls)
    # print(incorrect)

    get_paginated_data(cur, 2, 4)

    users_by_ascending(cur)

    sort_by_pattern(cur)

    # add_or_update(cur)

    # cur.execute("SELECT * FROM phonebook")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)

    cur.close()
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')

