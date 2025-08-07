import socket
import ast
from pymongo import MongoClient
from datetime import datetime

HOST = '0.0.0.0'
PORT = 5000

client = MongoClient("mongodb://mongodb:27017/")
db = client["messages_db"]
collection = db["messages"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket server listening on port", PORT)

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if data:
                try:
                    message = ast.literal_eval(data.decode())
                    message["date"] = datetime.now().isoformat()
                    collection.insert_one(message)
                    print("Saved message:", message)
                except Exception as e:
                    print("Error:", e)
