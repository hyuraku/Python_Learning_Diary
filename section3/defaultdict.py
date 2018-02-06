# とりあえず文字列を生成

s = "adsfadsfdafsdafsdfsadsfadasf"

# 文字列sの中にfやaがいくつあるのかを数える。

# 下のやり方をforやifを活用したもの
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)
#> {'a': 7, 'd': 7, 's': 7, 'f': 7}

# 下のはsetdefaultを活用した方法
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)
#> {'a': 7, 'd': 7, 's': 7, 'f': 7}

#下のはdefalutdictを活用している。
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)
#> defaultdict(<class 'int'>, {'a': 7, 'd': 7, 's': 7, 'f': 7})

d["f"]
#> 7
