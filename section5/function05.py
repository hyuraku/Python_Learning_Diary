def menu(entree='beef',drink='wine'):
    print(entree,drink)

menu(entree='beef',drink='wine')
#> beef wine

#この後menuに項目を使いしたい場合

def menu2(**kwargs):
    print(kwargs)

menu2(entree='beef',drink='wine')
#> {'entree': 'beef', 'drink': 'wine'}

d={
    'entree':'beef',
    'drink':'beer',
    'dessert':'ice'
}

menu2(**d)
#> {'entree': 'beef', 'drink': 'beer', 'dessert': 'ice'}

def menu3(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)

menu3('banana','apple','orange',entree='beef',drink='wine')
"""
banana
('apple', 'orange')
{'entree': 'beef', 'drink': 'wine'}
"""
