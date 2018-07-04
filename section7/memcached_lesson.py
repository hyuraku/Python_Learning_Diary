import sqlite3
import time

import memcache
#事前に memcached -vvを実行すること

db = memcache.Client(['127.0.0.1:11211'])

db.set('web_page','value1')
print(db.get('web_page'))
#>> value1

#一秒で消えるように設定する
db.set('web_page2','value2',time=1)
time.sleep(2)
#生成して一秒で消え、生成して2秒後に出力するコマンドなのでNoneとなる。
print(db.get('web_page2'))
#>> None

db.set('counter',0)
db.incr('counter',1)
print(db.get('counter'))
#>> 1
db.incr('counter',1)
print(db.get('counter'))
#>> 2

conn=sqlite3.connect('test_sqlite_2.db')
curs=conn.cursor()
curs.execute(
    'CREATE TABLE persons('
    'employ_id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()
conn.close()

def get_employ_id(name):
    employ_id=db.get(name)
    if employ_id:
        return employ_id
    curs.execute(
        'SELECT * FROM persons WHERE name = "{}"'.format(name)
    )

    #このpersonはタプル型
    person=curs.fetchone()
    if not person:
        raise Exception('No employ')
    employ_id,name=person
    db.set(name,employ_id,time=60)
    return employ_id

print(get_employ_id("Mike"))
