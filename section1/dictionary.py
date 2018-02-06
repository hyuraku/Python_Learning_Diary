#辞書型のデータの基本的な作り方。
d={'x':10,'y':20}

print(d)
print(type(d))
#> <class 'dict'>

print(d['x'],d['y'])
#xの値を100にする。
d['x']=100
print(d['x'],d['y'])
#> 100 20

#'z':200 を追加する
d['z']=200

#'1':50 を追加する
d[1]=50
print(d)
#> {'x': 100, 'y': 20, 'z': 200, 1: 50}

#これも辞書型データの作り方
d2=dict(a=10,b=20)
print(d2)
#> {'a': 10, 'b': 20}

#特定の型に使えるメソッドを調べるためにはhelp関数を使うと良い
#help(d2)

print(d2.keys())
#> dict_keys(['a', 'b'])
print(d2.values())
#> dict_values([10, 20])

d3={'a':100,'c':30}
d4=dict(a=30,b=40)
print(d2,d3)
#> {'a': 10, 'b': 20} {'a': 100, 'c': 30}

#d2にd3を追加、d2にあったaの値はd3の値になる。
d2.update(d3)
print(d2)
#> {'a': 100, 'b': 20, 'c': 30}

#aの値の出力するコマンド、基本は左のコマンド
print(d2['a'],d2.get('a'))
#> 100 100

#d2からaを削除、aの値を出力
d2.pop('a')
#> 100

#d2からaが削除されているのを確認する。
print(d2)
#> {'b': 20, 'c': 30}

#d2にkeyであるcがあるかを判定する。
#あればTrue、なければFalse
print('c' in d2)
#> True
