def s_hello():
    yield 'Hello1'
    yield 'Hello2'
    yield 'Hello3'

def g_hello():
    while True:
        y = yield from s_hello()
        yield y

g = g_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
