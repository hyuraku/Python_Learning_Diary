def outer(a,b):

    def inner():
        return a*b

    return inner

#print(outer(1,2))
#> <function outer.<locals>.inner at 0x10a9018c8>

f=outer(1,2)
r=f()
print(r)
#> 2

def circle_area_fun(pi):
    def circle_area(radius):
        return pi*radius*radius

    return circle_area

#まずpiに指定の数を代入する
cal=circle_area_fun(3.14)
cal2=circle_area_fun(3.141592)

print(cal(10))
#> 314.0
print(cal2(10))
#> 314.1592
