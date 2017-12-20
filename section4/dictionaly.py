#辞書型のデータの基本的な作り方。
d={'x':10,'y':20}

print(d)
print(type(d))

print(d['x'],d['y'])
d['x']=100
print(d['x'],d['y'])
d['z']=200
d[1]=50
print(d)

d2=dict(a=10,b=20)
print(d2)

#help(d2)

print(d2.keys())
print(d2.values())

d3={'a':100,'c':30}
d4=dict(a=30,b=40)
print(d2,d3)
d2.update(d3)
print(d2)
print(d2['a'],d2.get('a'))
d2.pop('a')
print(d2)
print('c' in d2)
print(d4)
