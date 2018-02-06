def outer(a,b):

    def plus(c,d):
        return c+d

    print(plus(a,b)+plus(b,a))

outer(2,2)
#> 8
#plus(2,3) #この関数は外では使えない。
