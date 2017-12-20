j=[1,2,3,4]
i=j
#i[0]=100
print(j)
print(i)

#x=j.copy()#こちらの方がわかりやすい。
x=j[:]
x[0]=100
print(j)
print(x)
#列をコピーするときは上記のコマンドをつかう

#idはアドレスを示す
print(id(j),id(i))
print(id(j),id(x))

n=[1,2,3,4,5,6,7,8,9]
#開始地点より１個とばしての表示
print(n[::2])
#終点より一個ずつ並べられる。
print(n[::-1])


n.append(10)
n.insert(0,0)
print(n)
n.pop()
n.pop(0)
print(n)

n=[1,2,3,3,2]
n.remove(2)
print(n)

s="My name is John"
to_split=s.split(' ')
print(to_split)

x='+'.join(to_split)
print(x)
