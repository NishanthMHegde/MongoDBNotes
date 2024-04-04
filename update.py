from pymongo import MongoClient

client = MongoClient("localhost", 27017)

#first select database
db = client.bookstore

#update one entry
db.books.update_one({'author': 'Shaun Pelling'}, {'$set' : {'rating' : 9}})

#update many entries
db.books.update_many({'author': 'Nana'}, {'$set' : {'rating' : 10}})

#update with push to arrays with push
db.books.update_one({'genre': {'$all' : ['biography' , 'adventure']}}, {'$push' : {'genre' : 'nonfiction'}})

#update with pull to arrays with pull
db.books.update_one({'genre' : {'$all' : ['biography', 'adventure']}}, {'$pull' : {'genre' : 'nonfiction'}})
