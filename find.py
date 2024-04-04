from pymongo import MongoClient

client = MongoClient("localhost", 27017)

#first select database
db = client.bookstore

#all books
print("\n\n\nFind all books")
books = db.books.find()
for book in books:
	print(book)

#all books with limit
print("\n\n\nFind all books with limit")
books = db.books.find().limit(4)
for book in books:
	print(book)

#simple find on single match
print("\n\n\nsimple find on single match")
books = db.books.find({"rating" : 10})
for book in books:
	print(book)

print("\n\n\nsort by ratings")
#sort by ratings
books = db.books.find({}).sort({"rating" : 1, "pages": 1})
for book in books:
	print(book)


#find by ratings
print("\n\n\nfind by ratings asc pages desc")
books = db.books.find({}).sort({"rating" : 1, "pages": -1})
for book in books:
	print(book)

#find by or operator
print("\n\n\n find by OR operator")
books = db.books.find({"$or": [{"rating" : {"$gt" : 8}}, {"pages" : {"$lt" : 300}}]})
for book in books:
	print(book)

#find by and operator
print("\n\n\n find by and operator")
books = db.books.find({"$and": [{"rating" : {"$gt" : 8}}, {"pages" : {"$lt" : 300}}]})
for book in books:
	print(book)

#find by in operator
print("\n\n\n find by in operator")
books = db.books.find({"rating" : {"$in" : [6,7]}})
for book in books:
	print(book)

#find by nin operator
print("\n\n\n find by in operator")
books = db.books.find({"rating" : {"$nin" : [6,7]}})
for book in books:
	print(book)

#find by nested document property
print("\n\n\n find by nested document property")
books = db.books.find({"reviews.name" : "Dhoni"})
for book in books:
	print(book)

print("\n\n\n")
#if fantasy is one among many genres, then it is fetched
books = db.books.find({"genre" : "fantasy"})
for book in books:
	print(book)

print("\n\n\n")
#if fantasy is the only genre, then it is fetched
books = db.books.find({"genre" : ["fantasy"]})
for book in books:
	print(book)

print("\n\n\n")
#if list of fantasies is part of the genre, then it is fetched. Other genre can also be part of the list
books = db.books.find({"genre" : {"$all" :["fantasy", "comedy"]}})
for book in books:
	print(book)

