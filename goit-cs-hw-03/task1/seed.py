# seed.py
import psycopg2
from faker import Faker
import random

fake = Faker()

conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="hw3", host="localhost", port="5434"
)
cur = conn.cursor()

# Створення 10 користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримати всі user_id і status_id
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Створення 30 завдань
for _ in range(30):
    title = fake.sentence(nb_words=4)
    description = fake.text() if random.choice([True, False]) else None
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id)
    )

conn.commit()
cur.close()
conn.close()

