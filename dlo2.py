#数据预处理


import os
import pandas as pd
import torch


#创建一个人工数据集，并处处存储在csv（逗号分隔值）文件
os.makedirs(os.path.join('..','data'),exist_ok=True)
data_file = os.path.join('..','data','hopuse_tiny.csv')
with open(data_file,'w') as f:
    f.write('NumRooms,Alley,Price\n') #列名
    f.write('NA,Pave,127500\n') #每行标傲世一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

#读取创建的CSV文件加载原始数据集

data = pd.read_csv(data_file)
print(data)

#处理缺失数据，插值和删除
#插值
inputs,outputs = data.iloc[:,0:2],data.iloc[:,2] #分割数据
inputs = inputs.fillna(inputs.mean()) #给缺失值赋值为均值
print(inputs)

#对于inputs中的类别之或者是离散值，我们将“NaN”视为一个类别
inputs = pd.get_dummies(inputs ,dummy_na=True )
print(inputs)

#因为inputs和outputs所有条目都是数值类型，所以可以将他们转换为张量格式
x,y = torch.tensor(inputs.values),torch.tensor(outputs.values)
print(x,y)