import json

j={
    "employee":
    [
        {"id": 111,"name":"Mike"},
        {"id": 222,"name":"Nancy"}
    ]
}

#まだ辞書型の出力である
print(j)

#jsonの型で出力される。
print(json.dumps(j))
a = json.dumps(j)

#loadsでjsonから辞書型に戻る。
print(json.loads(a))

with open('test.json','w') as f:
    #書き込むときはdump,sはつかない
    json.dump(j,f)

#辞書型で読み込み
with open('test.json','r') as f:
    print(json.load(f))
