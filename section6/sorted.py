ranking={
    'A':100,
    'B':75,
    'C':90
}

#ranking.getで数値を取り出す。
#reverseをTrueにすることで降順となる。
print(sorted(ranking,key=ranking.get,reverse=True))
