from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["form_database"]
collection = db["templates"]

templates = [
    {
        "name": "Order Form",
        "fields": {
            "lead_email": "email",
            "order_date": "date",
            "phone_number": "phone"
        }
    },
    {
        "name": "Contact Form",
        "fields": {
            "user_email": "email",
            "user_phone": "phone"
        }
    }
]

collection.insert_many(templates)
print("Шаблоны добавлены в базу данных MongoDB")
