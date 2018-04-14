import dbm

# with dbm.open('cache','c') as db:
#     db['key1']='value1'
#     db['key2']='value2'

with dbm.open('cache','r') as db:
    print(db.get('key1'))
