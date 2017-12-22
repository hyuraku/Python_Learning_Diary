def generate():
    for i in range(10):
        yield i

g=generate()
print(next(g))

#この表記だとジェネレーターになる
generate2=(i for i in range(10))
g2=generate2
print(next(g2))

#タプル型にしたい場合はtupleと表記する
generate3=tuple(i for i in range(10))
g3=generate3
print(type(g3))
