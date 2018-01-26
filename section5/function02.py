def menu(entree,drink,dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('beef','ice','beer')
"""
>
beef
ice
beer
"""

def menu(entree='beef',drink='wine',dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

menu()
"""
beef
ice
beer
"""

menu('chicken')
"""
chicken
wine
ice
"""

def test_func(x,l):
    l.append(x)
    return l

y=[1,2,3]
#引数の型はメソッドの指定に合わせましょう
test_func(100,y)
