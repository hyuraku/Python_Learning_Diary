t=(1,2,3,4,1,7)
print(t)
#> (1, 2, 3, 4, 1, 7)
print(type(t))
#> <class 'tuple'>

#指定の位置にある数理、マイナスの場合は末尾からカウント
print(t[0],t[-1])
#> 1 7

#最初の1から次の1まで何番目か
print(t.index(1,1))
#> 4

#tに1がいくつあるか
print(t.count(1))
#> 2

#タプルはカンマ（,）をつけた時点で成立する。
t2=1,2,3
print(type(t2))
#> <class 'tuple'>

t3=1,
t4=1
print(type(t3),type(t4))
#> <class 'tuple'> <class 'int'>

print(t3==t4)#これはfalseとなる
#> False

#タプルは書き換えさせないようにするものに使われる。
choice=('a','b','c')

answer=[]
choice.append('a')#かりに間違えてもエラー表記がでる。
answer.append('c')

print(choice)
print(answer)
