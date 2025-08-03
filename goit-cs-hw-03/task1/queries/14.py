import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q14():
    cur.execute("""
        SELECT u.fullname, COUNT(t.id) AS task_count
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id, u.fullname
    """)
    print("🔹 14. Кількість завдань для кожного користувача")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q14()       
    finally:
        cur.close()
        conn.close()