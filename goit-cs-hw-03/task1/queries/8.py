import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q8():
    cur.execute("SELECT * FROM users WHERE email LIKE '%@gmail.com'")
    print("🔹 8. Користувачі з email '@gmail.com'")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q8()       
    finally:
        cur.close()
        conn.close()