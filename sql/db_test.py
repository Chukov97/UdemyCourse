import sqlite3

conn = sqlite3.connect('students_db.db')
cursor = conn.cursor()

# students = [
#     ('Jane', 'Ostin', 19),
#     ('Jack', 'Scott', 22),
#     ('Bob', 'Green', 20)
# ]

# cursor.execute('CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);')
# insert_query = "INSERT INTO students VALUES ('James', 'Brown', 21);"

# insert_query = "INSERT INTO students VALUES (?, ?, ?);"

# for student in students:
#     cursor.execute(insert_query, student)
# cursor.execute(insert_query)
# cursor.executemany(insert_query, students)

# cursor.execute("SELECT * FROM students WHERE first_name IS 'James';")

# for row in cursor:
#     print(row)

# print(cursor.fetchall())
# cursor.execute("UPDATE students SET last_name = 'Austen' WHERE last_name IS 'Ostin';")

cursor.execute("DELETE FROM students WHERE last_name IS 'Green';")

conn.commit()
conn.close()
