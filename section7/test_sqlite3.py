import sqlite3

#test_sqlite3.dbを開く、無ければ生成する。
conn = sqlite3.connect('test_sqlite3.db')

#メモリー上にDBを作成する
#conn = sqlite3.connect(':memory:')

curs=conn.cursor()

# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING )')
# conn.commit()

#データの挿入
# curs.execute('INSERT INTO persons(name) values("MIKE")')
# conn.commit()

#全データの確認
# curs.execute('SELECT * FROM persons')
# print(curs.fetchall())

#データの上書き
curs.execute('UPDATE persons set name = "Michel" where name ="MIKE"')
conn.commit()

#全データの確認
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

#そして閉じる
curs.close()
conn.close()
