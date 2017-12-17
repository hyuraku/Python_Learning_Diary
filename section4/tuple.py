t=(1,2,3,4,1,7)
print(t)
print(type(t))
print(t[0],t[-1])
print(t.index(1,1))
print(t.count(1))

t2=1,2,3
print(type(t2))
#タプルはカンマ（,）をつけた時点で成立する。
t3=1,
t4=1
print(t3==t4)#これはfalseとなる

#タプルは書き換えさせないようにするものに使われる。

choice=('a','b','c')

answer=[]
choice.append('a')#かりに間違えてもエラー表記がでる。
answer.append('c')

print(choice)
print(answer)
