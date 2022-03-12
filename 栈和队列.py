from collections import deque

x = [9,7,8]
print(x)
x.append(666)
print(x)
x.pop()
print(x)


y = deque(x)
print(y)
y.append(666)
print(y)
y.popleft()
print(y)
