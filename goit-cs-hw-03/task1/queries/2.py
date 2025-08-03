import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q2():
    cur.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')")
    print("🔹 2. Завдання зі статусом 'new'")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q2()       
    finally:
        cur.close()
        conn.close()