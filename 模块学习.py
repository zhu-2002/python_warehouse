#随机数模块学习
#随机数模块
import random
#正则表达式模块
import re

#在[0,100]的范围里面产生一个步长为5的随机数0？）
#(start,stop,step)
print(random.randrange(0,100,5))

#从一个非空数列中选择一个随机选项
x = range(0,100)
print(random.choice(x))

#将一个序列随机打乱,处理的是原list，操作的对象一定是list
z = list(x)
random.shuffle(z)
print(z)

#返回从中提序列中唯一元素，不放回
z = random.sample(z,3)
print(z)

#[1,10]产生随机浮点数
print(random.uniform(1,10))

#在字符中查找模式
demo = 'My name is Zenos ,z I am 12 years old now'
print(re.search(",",demo))
print(re.search("[zZ]",demo))

#在字符串中开始匹配模式
r = re.compile(":")
x = '23sdas:dfsaf'
#只能匹配第一个字符
print(r.match(x))
print(r.split(x))
#列表形式返回匹配项
#创建模式对象
