day=['Mon','Tue','Wed']
drink=['beer','cola','water']

menu={}

#これはforとzipを用いた辞書型データ生成
for x,y in zip(day,drink):
    menu[x]=y

print(menu)
#> {'Mon': 'beer', 'Tue': 'cola', 'Wed': 'water'}

#こちらは辞書内包表記
menu2={x:y for x,y in zip(day,drink)}
print(menu2)
#> {'Mon': 'beer', 'Tue': 'cola', 'Wed': 'water'}
