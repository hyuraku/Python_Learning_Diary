t=[1,2,3,4,5]

line01=[]

#for文をつかってtの値を空のリストに代入する方法
for i in t:
    line01.append(i)

print(line01)

#リスト内包表記
line02=[i for i in t]
print(line02)

#例えばif文内に制御構文があるとする。
line03=[]
for i in t:
    if i%2==0:
        line03.append(i)

print(line03)

#リスト内包表記でも制御構文が書ける。
line4=[i for i in t if i%2==0]
print(line4)

#やろうと思えば長くできるけど、可読性が低くなるので
#せめてforやifが一つだけの時にしよう

p=(1,2,3,4)
q=(5,6,7,8,9)

line05=[i*j for i in p for j in q]
print(line05)
