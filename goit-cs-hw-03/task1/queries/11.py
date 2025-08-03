import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q11():
    cur.execute("""
        SELECT t.* FROM tasks t
        JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE '%@example.com'
    """)
    print("🔹 11. Завдання користувачів з email '@example.com'")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q11()       
    finally:
        cur.close()
        conn.close()