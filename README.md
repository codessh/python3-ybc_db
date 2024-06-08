# python3-ybc_db
This is a Practical Python 3 Database Module!
# How can I use?
1.Download 7z compressed package and decompress it.
2.Run "install.py" (If necessary, you can back up the files that depend on this installation)
3.Waiting for MongoDB to start (You don't need to install MongoDB)
4.Enjoy!(Run test.py to check the program is running normally)
# Functions
database = ybc_db.create_db(name)
c_todo = database.collection(name)
c_todo.insert_one({'123':"456"})
