#可迭代对象就是可以逐个遍历的对象
#迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一 个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。
#inter（）构造迭代器
x = ['a','b','c']
i = iter(x)
print(next(i))
print(next(i))
print(next(i))
#生成器
# 一边循环一边计算的机制，成为生成器
#yield
def gen(n):
    for i in range(n):
        yield i*i
#gen = ( i*i for i in range(5) )
y = gen(5)
print(list(y))
