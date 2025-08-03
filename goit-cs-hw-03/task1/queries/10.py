import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q10():
    cur.execute("""
        SELECT s.name, COUNT(t.id) AS task_count
        FROM status s
        LEFT JOIN tasks t ON s.id = t.status_id
        GROUP BY s.name
    """)
    print("🔹 10. Кількість завдань за статусом")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q10()       
    finally:
        cur.close()
        conn.close()