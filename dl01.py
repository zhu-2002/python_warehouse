import torch
#张量表示一个数值组成的数组，这个数组可能有多个维度
x = torch.arange(12)

print(x)

print(x.shape)#张量的形状
print(x.numel())#张量的元素总数
print(x.reshape(3,4))#改变一个张量的形状而不改变元素的属性和元素值
print(torch.ones((2,3,4)))
print(torch.zeros((2,3,4)))#使用全部0，1或者其他常量从特定分布中随机采样数字
#torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])#使用含有数值的列表来作为张量中每个元素赋予特定值
x = torch.tensor([1.0,2,4,8])
y = torch.tensor([2,2,2,2])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)


print(torch.exp(x))#按按元素方式应用更多的计算

#将多个张量连接在一起
x = torch.arange(12,dtype=torch.float32).reshape((3,4))
y = torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
print(torch.cat((x,y),dim=0))#按行
print(torch.cat((x,y),dim = 1))#按列
print(x.sum()) #求和

#广播机制
a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))
print(a+b)

#元素的访问
print(x[-1])#最后一行
print(x[1:3])#一到二行

#多个元素的赋值
x[0:2,:] = 12 #0到1行每个元素都赋值为12
print(x)

#执行原地操作
z = torch.zeros_like(y)
print(id(z))
z = x+y
print(id(z))

#转换为Numpy张量
a = x.numpy()
b = torch.tensor(a)
print(type(a))
print(type(b))

#将大小为1的张量转换为Python标量
a =torch.tensor([3.5])
print(a,a.item(),float(a),int(a))

