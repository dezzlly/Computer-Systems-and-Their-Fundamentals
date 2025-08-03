import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q12():
    cur.execute("SELECT * FROM tasks WHERE description IS NULL")
    print("🔹 12. Завдання без опису")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q12()       
    finally:
        cur.close()
        conn.close()