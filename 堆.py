#特点
#堆是一个二叉树，他的没哦一个父节点的值都会小于等于所有子节点的值
#使用数组实现：从0开始计数，对于所有的k，都有heap[k] <= heap[2*k+1]和heap[k] <= heap[2*k+2]
#最小的元素是根节点：heap[0]
import heapq
x = [1,2,3,4,5,6,7,8,9,10]
print(x)
#构造一个堆，把一个列表转化成堆
heapq.heapify(x)
print(x)
#在堆中插入一个值
heapq.heappush(x,0)
print(x)
#在堆中弹出最小值
print(heapq.heappop(x))
print(x)
#先将item放入堆中，然后弹出去并返回最小元素
#heapq.heappushpop(heap,item)
item = 11
min = heapq.heappushpop(x,item)
print(x)
print(min)
#先弹出堆中的最小元素，同时放入新的item，再排序
#heapq.heapreplace(heap,item)
item = 11
min = heapq.heapreplace(x,item)
print(x)
print(min)

y = [123,424,4356,4564,645,20,52]
#将多个已经排序的输出合并为一个已排序的输出
print(list(heapq.merge(x,y)))

#从iterable所定义的数据集中分会前n个最大元素组成的列表
lg = heapq.nlargest(4,y)
print(lg)
#从iterable所定义的数据集中返回前n个最小元素组成的列表
sm = heapq.nsmallest(4,y)
print(sm)