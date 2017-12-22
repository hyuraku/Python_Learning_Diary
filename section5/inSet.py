s=set()

#これは通常の集合型データの生成
for i in range(10):
    s.add(i)

print(s)

#集合内包表記
s2={i for i in range(10)}
print(s2)
