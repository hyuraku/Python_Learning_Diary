def menu(entree,drink,dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('beef','ice','beer')

def menu(entree='beef',drink='wine',dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

menu()
menu('chicken')

def test_func(x,l):
    l.append(x)
    return l

#y=[1,2,3]
test_func(100)
