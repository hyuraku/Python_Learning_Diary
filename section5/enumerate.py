i=0
for fruit in ['apple','banana','orange']:
    print(i,fruit)
    i+=1

for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)

for fruit in enumerate(['apple','banana','orange']):
    print(fruit)
