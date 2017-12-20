time=['morning','afternoon','night']

#for文による出力
'''
for i in time:
    print(i)
'''

def tell_time():
    yield 'morning'
    yield 'afternoon'
    yield 'night'

'''
for t in time:
    print(t)
'''

t=tell_time()
print(next(t))
print(next(t))
print(next(t))
