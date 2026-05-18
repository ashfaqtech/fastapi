from db import get_connection

conn = get_connection()
cursor = conn.cursor()

# Create table
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()


# ➕ CREATE
def create_student(name, age):
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return {"message": "Student created"}


# 📖 READ ALL
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


# 📖 READ ONE
def get_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    return cursor.fetchone()


# ✏️ UPDATE
def update_student(student_id, name, age):
    cursor.execute("UPDATE students SET name=?, age=? WHERE id=?", (name, age, student_id))
    conn.commit()
    return cursor.rowcount


# ❌ DELETE
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    return cursor.rowcount