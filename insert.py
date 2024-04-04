from pymongo import MongoClient

client = MongoClient("localhost", 27017)

#first select database
db = client.bookstore

#insert one item
# print("\n\n\ninsert one item")
# db.books.insert_one({"author": "Mike Buchy", "title":"Egg Story", "rating": 8, "pages": 350 , "genre": ["fantasy", "adventure"], "reviews": [{"name": "Bucky", "body": "engaging"}]})

#insert many items
# print("\n\n\ninsert many items")
# db.books.insert_many([{"author": "Mike Bottom", "title":"Cactus Jack in Bangalore", "rating": 7, "pages": 250 , "genre": ["fantasy", "comedy"], "reviews": [{"name": "Gilbert", "body": "soul touching"}]},
# {"author": "Jadeja", "title":"Birth of all rounder", "rating": 10, "pages": 550 , "genre": ["biography", "adventure"], "reviews": [{"name": "Dhoni", "body": "exciting"}]}])
	