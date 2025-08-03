import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q13():
    cur.execute("""
        SELECT u.fullname, t.title FROM users u
        JOIN tasks t ON u.id = t.user_id
        WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress')
    """)
    print("🔹 13. Користувачі та завдання у статусі 'in progress'")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q13()       
    finally:
        cur.close()
        conn.close()