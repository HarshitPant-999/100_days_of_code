import sqlite3

db = sqlite3.connect("books-collection.db") #CREATING CONNECTION TO A NEW DATABASE

cursor = db.cursor()

cursor.execute("INSERT INTO books VALUES(1, 'Sherlock Holmes', 'Sir Arthur Conan Doyle' , '7.5')")
db.commit()
