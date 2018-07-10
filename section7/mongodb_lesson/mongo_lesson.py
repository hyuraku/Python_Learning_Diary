import datetime

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name':'customer1',
    'pip':['python','java','go'],
    'info':{'os':'mac'},
    'date': datetime.datetime.utcnow()
}

stack2 = {
    'name':'customer2',
    'pip':['python','ruby','go'],
    'info':{'os':'linux'},
    'date': datetime.datetime.utcnow()
}

db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id
stack_id = db_stacks.insert_one(stack2).inserted_id

print(stack_id,type(stack_id))
from bson.objectid import ObjectId
str_stack_id = '5b3cdc0cbbca0ab9451fa1fa'
print("###########")
print(db_stacks.find_one({'_id':stack_id}))
print(db_stacks.find_one({'_id':ObjectId(str_stack_id)}))
# >>5b3cdc0cbbca0ab9451fa1fa <class 'bson.objectid.ObjectId'>
# ###########
# {'_id': ObjectId('5b3cdc0cbbca0ab9451fa1fa'), 'name': 'customer1', 'pip': ['python', 'java', 'go'], 'info': {'os': 'mac'}, 'date': datetime.datetime(2018, 7, 4, 14, 39, 8, 881000)}
# {'_id': ObjectId('5b3cdc0cbbca0ab9451fa1fa'), 'name': 'customer1', 'pip': ['python', 'java', 'go'], 'info': {'os': 'mac'}, 'date': datetime.datetime(2018, 7, 4, 14, 39, 8, 881000)}
