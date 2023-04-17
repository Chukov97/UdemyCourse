import sqlite3

conn = sqlite3.connect('users_db.db')
cursor = conn.cursor()

# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT);"

# cursor.execute(create_query)

users = [

    ('jack123', 'faf0gshs'),
    ('janepretty444', 'afgwte42q'),
    ('bobman123', 'agrgou4jlj')

]

# insert_query = "INSERT INTO users VALUES (?, ?)"
# cursor.executemany(insert_query, users)

user_name = input('Input your username')
user_password = input('Input your password')

# select_query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND user_password = '{user_password}'"
select_query = f"SELECT * FROM users WHERE user_name = ? AND user_password = ?"
cursor.execute(select_query, (user_name, user_password))
data = cursor.fetchone()
if data:
    print('You are logged in')
else:
    print('Please try again')

conn.commit()
conn.close()
