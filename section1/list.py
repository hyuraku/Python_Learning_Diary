#リスト型は参照型なので
#代入だけで複製はできない。
j=[1,2,3,4]
i=j
i[0]=100
print(j)
#>[100, 2, 3, 4]

print(i)
#>[100, 2, 3, 4]

#複製するための2つのコマンド
#後者の方がわかりやすい。
x=j.copy()
x=j[:]
x[0]=500
print(j)
#> [100, 2, 3, 4]

print(x)
#> [500, 2, 3, 4]


#idはアドレスを示す
print(id(j),id(i))
#> 4568621512 4568621512

print(id(j),id(x))
#> 4568621512 4568621576

n=[1,2,3,4,5,6,7,8,9]
#開始地点より１個とばしての表示
print(n[::2])
#> [1, 3, 5, 7, 9]

#終点より一個ずつ並べられる。
print(n[::-1])
#> [9, 8, 7, 6, 5, 4, 3, 2, 1]

#末尾に10を追加
n.append(10)

#0番目に0を追加
n.insert(0,0)
print(n)
#> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#末尾の数を削除し、その数を出力
n.pop()
#> 10

#指定の位置の数を削除、その数を出力
n.pop(0)
print(n)
#> [1, 2, 3, 4, 5, 6, 7, 8, 9]

n=[1,2,3,3,2]
#指定の位置の数を削除、その数を出力
n.remove(2)
print(n)
#> [1, 3, 3, 2]

s="My name is John"
#指定の記号で分けて、リストにする。
to_split=s.split(' ')
print(to_split)
#> ['My', 'name', 'is', 'John']

#+を区切り文字にして連結
x='+'.join(to_split)
print(x)
#> My+name+is+John
