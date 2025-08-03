import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="hw3",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def q1():
    cur.execute("SELECT * FROM tasks WHERE user_id = 1")
    print("🔹 1. Завдання для user_id = 1")
    print(cur.fetchall())

if __name__ == "__main__":
    try:
        q1()       
    finally:
        cur.close()
        conn.close()