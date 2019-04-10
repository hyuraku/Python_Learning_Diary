def g_hello():
    while True:
        y = yield 'Hello'
        yield y

g = g_hello()
print(next(g))
print(g.send('plus'))
print(next(g))
print(g.send('minus'))

# >Hello
# >plus
# >Hello
# >minus
