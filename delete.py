from pymongo import MongoClient

client = MongoClient("localhost", 27017)

#first select database
db = client.bookstore

db.books.delete_one({'author' : 'Shaun Pelling'})

db.books.delete_many({'rating' : {'$lt' : 8}})