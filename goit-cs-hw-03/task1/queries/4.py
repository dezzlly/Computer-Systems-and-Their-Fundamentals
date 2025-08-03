import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q4():
    cur.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
    print("🔹 4. Користувачі без завдань")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q4()       
    finally:
        cur.close()
        conn.close()