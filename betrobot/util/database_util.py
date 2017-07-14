import pymongo


db_name = 'betrobot'

client = pymongo.MongoClient()
db = client[db_name]
