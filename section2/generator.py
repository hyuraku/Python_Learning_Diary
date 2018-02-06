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
#nextによってあらかじめyieldで指定した値を出力する。
print(next(t))
#> morning
print(next(t))
#> afternoon
print(next(t))
#> night
print(next(t))
"""
>
--<omit>--
StopIteration:
"""
