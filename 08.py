import random
import torch


#根据带有带有噪声的线性模型构造一个人造数据集。我们使用线性模型参数w = [2,-3,4]T , b = 4.2 和噪声项生c成数据据集以及其标签：y = Xw + b + c
def sy_data(w,b,num_examples):
    x = torch.normal(0,1,(num_examples,len(w) ) )  #均值为0，方差为1的随机数，n个样本，按照w的长度为列数排列
    y = torch.matmul(x,w) + b                      #矩阵相乘
    y += torch.normal(0,0.01,y.shape)              #随机噪音，均值为0，方差为0.01，形状和y的长度一样
    return x,y.reshape((-1,1))                     #将X和Y做成一个列向量返回

true_w = torch.tensor([2,-3.4])
true_b = 4.2
features,labels = sy_data(true_w,true_b,1000)


#定义一个data_iter函数，该函数接受批量大小，特征矩阵和标签向量作为输入，生成大小为batch_size的小批量
def data_iter( batch_size , features , labels ):
    num_examples = len( features )
    indices = list( range ( num_examples ) )
    random.shuffle( indices )  #将下标随机打乱
    for i in range( 0 , num_examples , batch_size ):
        batch_indices = torch.tensor( indices[i:min( i + batch_size , num_examples )] )
        yield features[batch_indices] , labels[batch_indices] #迭代器，每次循环都会返回这两个值，直到循环结束

batch_size = 10 ;
for x,y in data_iter(batch_size,features,labels):
    print(x,'\n',y)
    break ;


#定义初始化模型参数
w = torch.normal(0,0.01,size=(2,1),requires_grad=True)
b = torch.zeros(1,requires_grad=Ture)

#定义模型
def linreg(x,w,b):
    """线性回归模型。"""
    return torch.matmul(x,w) + b

#定义损失函数
def squared_loss(y_hat,y):
    """均方损失。"""
    return ( y_hat - y.reshape( y_hat.shape ) ) ** 2 / 2

#定义优化算法
def sgd( params , lr , batch_size ) :
    """"小批量随机梯度下降"""
    with torch.no_grad() :
        for param in params :
            param -= lr * param.grad / batch_size
            param.grad.zero_()  #将梯度手动调零

lr = 0.03
num_epochs  = 3
net = linreg
loss = squared_loss

for epoch in range( num_epochs ):
    for x , y in data_iter( batch_size , features , labels ):
        l = loss( net( x,w,b ) , y )
        l.sum().backward()
        sgd( [w , b] , lr , batch_size ) #使用参数的梯度更新参数
    with torch.no_grad() :
        train_l = loss( net( features,w,b) , labels )
        print(f'epoch{epoch+1}.loss{float(train_l.mean()):f }')

#比较真实参数和通过训练学到的参数来评估训练的成功程度
print(f'w的估计误差：{true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差：{true_b - b }')


#线性回归模型的简洁实现
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

true_w = torch.tensor( [ 2 , -3.4 ] )
true_b = 4.2
features , labels = d2l.sy_data(true_w,true_b,1000)

def load_array( data_arrays , batch_size , is_train = True ) :
    """构造一个pytorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays) #*表示列表元素分别当作参数穿进去
    return data.DataLoader( dataset , batch_size , shuffle = is_train )

batch_size = 10
data_iter = load_array( (features,labels) , batch_size )

next(iter(data_iter))

from torch import nn
net = nn.Sequential(nn.Linear(2,1))
net[0].weight.data.normal_(0,0.01)
net[0].bias.data.fill_(0)

#计算均方误差使用的是MSELoss类，也称作平方L2范数
loss = nn.MSELoss()
#实例化SGD实例
trainer = torch.optim.SGD( net.parameters() , lr = 0.03 )

num_epochs = 3
for epoch in range( num_epochs ) :
    for x , y in data_iter :
        l = loss( net(x) , y )
        trainer.zers_grad()
        l.backward()
        trainer.step()
    l = loss( net( features ) , labels )
    print( f'epoch{epoch + 1},loss{l:f}')
