import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q3():
    cur.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 5 RETURNING *")
    print("🔹 3. Оновлення статусу завдання з id = 5")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q3()       
    finally:
        cur.close()
        conn.close()