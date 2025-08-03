import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q6():
    cur.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
    print("🔹 6. Завдання, які ще не завершено")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q6()       
    finally:
        cur.close()
        conn.close()