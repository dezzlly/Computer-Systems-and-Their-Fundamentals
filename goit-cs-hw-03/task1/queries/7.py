import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q7():
    cur.execute("DELETE FROM tasks WHERE id = 3 RETURNING *")
    conn.commit()
    print("🔹 7. Видалено завдання з id = 3")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q7()       
    finally:
        cur.close()
        conn.close()