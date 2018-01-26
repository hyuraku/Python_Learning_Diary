i=0

これは普通のfor_inの文
for fruit in ['apple','banana','orange']:
    print(i,fruit)
    i+=1
"""
>
0 apple
1 banana
2 orange
"""

for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)
"""
>
0 apple
1 banana
2 orange
"""

#　iを使わなくても同様の出力結果
for fruit in enumerate(['apple','banana','orange']):
    print(fruit)
"""
>
(0, 'apple')
(1, 'banana')
(2, 'orange')
"""
