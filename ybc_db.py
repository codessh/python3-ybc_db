# 从猿编程的程序文件中提取
# 这些代码是叔叔阿姨们的劳动成果, 
# 禁止未标注原作者的搬运,代码仅供参考、研究和使用
import pymongo
from bson.objectid import ObjectId


class ParamError(Exception):
    """自定义异常"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Collection:
    """封装pymongo的collection类"""
    def __init__(self, collection):
        self.collection = collection

    def insert_one(self, data=None):
        if data is None:
            raise ParamError('请传入要添加的数据')

        # 生成字符串类型的ID
        # TODO 这里的ID名字用哪个？(_id, id)
        data['_id'] = str(ObjectId())

        try:
            self.collection.insert_one(data).inserted_id
            return True
        except Exception as e:
            print(e)
            return False

    def insert_many(self, data=None):
        if data is None:
            raise ParamError('请传入要添加的数据')

        # 生成字符串类型的ID
        for each in data:
            each['_id'] = str(ObjectId())
        try:
            self.collection.insert_many(data)
            return True
        except Exception as e:
            print(e)
            return False

    def find_one(self, data=None):
        if data is None:
            raise ParamError('请传入要查询的数据')
        
        return self.collection.find_one(data)

    def find_all(self, data=None):
        result = self.collection.find(data)
        return list(result)
    
    def update_one(self, query_data=None, update_data=None):
        if (query_data is None) or (update_data is None):
            raise ParamError('请输入更新条件和数据')

        # $inc 只能用于数字
        update_data = {'$set': update_data}

        try:
            result = self.collection.update_one(query_data, update_data)
            return True
        except Exception as e:
            print(e)
            return False

    def update_all(self, query_data=None, update_data=None):
        if (query_data is None) or (update_data is None):
            raise ParamError('请输入更新条件')

        # $inc 只能用于数字
        update_data = {'$set': update_data}

        try:
            result = self.collection.update_many(query_data, update_data)
            # print(result.matched_count)
            return True
        except Exception as e:
            print(e)
            return False
        
    def delete_one(self, data=None):
        if data is None:
            raise ParamError('“请输入删除条件')

        try:
            self.collection.delete_one(data)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_all(self, data=None):
        if data is None:
            raise ParamError('“请输入删除条件')
        try:
            self.collection.delete_many(data)
            return True
        except Exception as e:
            print(e)
            return False


class DB:
    """封装pymongo的db类"""
    def __init__(self, db):
        self.db = db
    
    def collection(self, collection_name=None):
        if collection_name is None:
            raise ParamError('需要传入集合名称')
        return Collection(self.db[collection_name])
         

def create_db(name=None):
    # 创建数据库表
    if name is None:
        raise ParamError('需要传入数据库名称')

    client = pymongo.MongoClient()
    db = client[name]
    return DB(db)


