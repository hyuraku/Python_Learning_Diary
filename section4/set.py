a={1,2,2,3,3,4,4}
b={2,3,3,5}

#aとbにあるもの。
print(a,b)

#aにあってbにないものと、その逆
print(a-b,b-a)

#aとbに共通してあるもの
print(a&b)

#aとbにあって重複していないもの
print(a^b)

#aとbにあるもの
print(a|b)

s={1,2,3,4,5}
s.add(6)
print(s)
s.remove(6)
print(s)

#変数のコードスタイルは上に書くべき
