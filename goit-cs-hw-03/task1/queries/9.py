import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q9():
    cur.execute("UPDATE users SET fullname = 'Оновлене Ім’я' WHERE id = 1 RETURNING *")
    conn.commit()
    print("🔹 9. Оновлено ім’я користувача з id = 1")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q9()       
    finally:
        cur.close()
        conn.close()