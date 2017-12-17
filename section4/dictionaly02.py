x={'a':1}
y=x

print(id(x),id(y))

y=x.copy()
y['a']=100
print(id(x),id(y))
