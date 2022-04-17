# -*- coding: utf-8 -*-
"""
  @CreateTime	:  2022/04/17 15:52:05
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
"""


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):  # 需要重写hash函数，自定义的hash方式，用于当x,y hash相同时不会出现多个key
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


d = {}
pos = Position(0, 1)
pos2 = Position(0, 1)
# 自定义__eq__函数后可以用于比较两个object对象之间是否相等
# print(pos == pos2)

# 但是再用做dictionary的key就会报错
"""
省流：自定义类型做dict的key，必须要有__hash__方法（自己定义的，或是继承自object的）。
dict判断两个key是不是一个key：先比较id，再比较hash，再进行__eq__比较。

在没有重写__eq__函数时，类只会去比较两个变量的id，如果id不同，也就不同。比如没有__eq__时上面例子的结果是
id(pos) = 4341486480 id(pos2)=4341486648 
{<__main__.Position object at 0x102c5d390>: 1, <__main__.Position object at 0x102c5d438>: 2}
"""
d[pos] = 1

# pos2 = Position(0, 1)
d[pos2] = 2
print(id(pos), id(pos2), d)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other): # 认为跟其他所有的永远不相同
        return False


d = {}
pos = Position(0, 1)
pos2 = pos
print(pos == pos2)

d[pos] = 1
d[pos2] = 2
print(d)
