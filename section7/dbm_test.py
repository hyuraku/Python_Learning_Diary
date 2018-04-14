import dbm

#dbを書き込みできる状態で開く
# with dbm.open('cache','c') as db:
#     db['key1']='value1'
#     db['key2']='value2'

#dbを読み込みできる状態で開く
with dbm.open('cache','r') as db:
    print(db.get('key1'))
