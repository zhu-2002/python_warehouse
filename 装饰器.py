#特殊的闭包，外函数的参数是另一个函数
def show(function) :
    def temp(x,y) :
        print('=======')
        z = function(x,y)
        return z
    return temp

def myadd(x,y):
    return x+y
myadd = show(myadd)
print(myadd(3,4))

#优化
@show
def mydivide(x,y):
    return x/y
print(mydivide(3,4))

#接受不同的参数
#*args:搜集所有位置参数
#**kwargs:搜集所有关键值参数，就像字典之类
#def funx(*args,**kwargs):
#    print(args,kwargs)