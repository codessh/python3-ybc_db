# python3-ybc_db

一个让小白更方便管理MongoDB的Python3模块！

# 我怎么用嘞 ..(｡•ˇ‸ˇ•｡)… ？

1.解压Release的ybc_db.7z

2.运行install.py(依赖安装完成后，程序会自动删除该文件，你可以备份一个）

3.如果有提示按回车即可，然后静静等待压缩包内MongoDB运行(应该是一个字符填满窗口的东西)

4.然后就尽情的玩耍吧！

# 功能

'''创建数据库'''

database = ybc_db.create_db(name)

'''创建新集合'''

c_todo = database.collection(name)

'''创建新数据'''

c_todo.insert_one({'123':"456"})

'''搜索单个数据'''

get = c_todo.find_one({'age':11})

'''获取所有数据'''

get = c_todo.find_all()
