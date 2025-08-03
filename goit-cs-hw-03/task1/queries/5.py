import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q5():
    cur.execute("""INSERT INTO tasks (title, description, status_id, user_id)
                   VALUES ('Новий таск', 'Опис таску', (SELECT id FROM status WHERE name = 'new'), 2)
                   RETURNING *""")
    conn.commit()
    print("🔹 5. Додано нове завдання для user_id = 2")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q5()       
    finally:
        cur.close()
        conn.close()