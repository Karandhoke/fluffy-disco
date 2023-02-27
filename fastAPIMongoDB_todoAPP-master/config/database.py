from pymongo import MongoClient



client = MongoClient("mongodb+srv://karandhoke:<password>@cluster0.tpxalbn.mongodb.net/?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]
