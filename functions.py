import ybc_db

# Create new Database 新建数据库
db = ybc_db.create_db('my_database')
# Create new Collection 创建新集合
coll = db.collection('my_collection')

# Create new data(dictionary) 创建新数据（字典形式）
coll.insert_one({'age':11,'name':'codessh'})
# Find all data(return a list) 输出所有数据（列表形式）
alld = coll.find_all()
# Find one data 搜索一条数据
oned = coll.find_one({'name':'MCSRC(Anti-Mini')})
# Delete one data(search) 删除一个数据（需要查询条件）
coll.delete_one({'age':10,'name':'MCSRC(Anti-Mini)'})# id:'114514'
