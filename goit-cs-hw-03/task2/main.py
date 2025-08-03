from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


MONGO_URI = "mongodb+srv://dezzly21:dezzly21@cluster0.mz8wvko.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["cat_database"]
collection = db["cats"]

db = client.cats

if collection.count_documents({}) == 0:
    many_cats = collection.insert_many([
        {"name": "Lama", "age": 2, "features": ["ходить в лоток", "не дає себе гладити", "сірий"]},
        {"name": "Liza", "age": 4, "features": ["ходить в лоток", "дає себе гладити", "білий"]},
        {"name": "Boris", "age": 12, "features": ["ходить в лоток", "не дає себе гладити", "сірий"]},
        {"name": "Murik", "age": 1, "features": ["ходить в лоток", "дає себе гладити", "чорний"]}
    ])
    print("✅ Коти додані до бази.")
else:
    print("ℹ️ Коти вже існують у базі.")

def read_all_cats():
    try:
        cats = list(collection.find())
        if not cats:
            print("База даних порожня.")
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Помилка при читанні: {e}")


# 📖 READ: Знайти кота за ім'ям
def find_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з іменем {name} не знайдений.")
    except PyMongoError as e:
        print(f"Помилка пошуку: {e}")


# 🆕 CREATE: Додати нового кота
def create_cat(name, age, features):
    try:
        result = collection.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
        print(f"Кота додано з ID: {result.inserted_id}")
    except PyMongoError as e:
        print(f"Помилка створення: {e}")


# 🔁 UPDATE: Оновити вік кота
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print(f"Вік кота {name} оновлено.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка оновлення віку: {e}")


# 🔁 UPDATE: Додати характеристику
def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count:
            print(f"Характеристику додано коту {name}.")
        else:
            print(f"Кота з ім'ям {name} не знайдено або характеристика вже існує.")
    except PyMongoError as e:
        print(f"Помилка оновлення характеристик: {e}")


# ❌ DELETE: Видалити кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кота {name} видалено.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка видалення: {e}")


# ❌ DELETE: Видалити всіх котів
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except PyMongoError as e:
        print(f"Помилка при видаленні всіх записів: {e}")



def menu():
    while True:
        print("\n--- Меню ---")
        print("1. Вивести всіх котів")
        print("2. Знайти кота за ім'ям")
        print("3. Додати нового кота")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            read_all_cats()
        elif choice == "2":
            name = input("Введіть ім'я кота: ")
            find_cat_by_name(name)
        elif choice == "3":
            name = input("Ім'я: ")
            age = int(input("Вік: "))
            features = input("Характеристики (через кому): ").split(",")
            create_cat(name, age, [f.strip() for f in features])
        elif choice == "4":
            name = input("Ім'я кота: ")
            new_age = int(input("Новий вік: "))
            update_cat_age(name, new_age)
        elif choice == "5":
            name = input("Ім'я кота: ")
            feature = input("Нова характеристика: ")
            add_feature_to_cat(name, feature.strip())
        elif choice == "6":
            name = input("Ім'я кота для видалення: ")
            delete_cat_by_name(name)
        elif choice == "7":
            confirm = input("Ви впевнені? (так/ні): ")
            if confirm.lower() == "так":
                delete_all_cats()
        elif choice == "0":
            break
        else:
            print("Невірна опція. Спробуйте ще.")


if __name__ == "__main__":
    menu()