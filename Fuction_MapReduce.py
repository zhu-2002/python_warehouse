#map（函数名，对象）
def fun(x):
    return x**2
a = [1,2,3,4,5,6,7,8,9]
print(list(map(fun,a)))

#reduce（函数名，对象）1
from functools import reduce
def maxn(x,y):
    if x>y :
        z =x
    else :
        z = y
    return z
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(maxn,b))
