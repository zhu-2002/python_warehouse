#特点：
# 函数中有函数
# 内函数使用外函数的参数
# 外函数的返回值是内函数
def price( unitprice ) :
    def computer(weight) :
        return (weight-0.1)*unitprice
    return computer
apple = price(3)
print(apple(10.1))

banana = price(5)
print(banana(10.1))