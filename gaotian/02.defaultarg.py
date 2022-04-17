# -*- coding: utf-8 -*-
"""
  @CreateTime	:  2022/04/16 11:59:46
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
"""


class Player(object):
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items
        print(id(self.items))


"""
Alice和Bob因为没有传值，都使用了默认值items=[]，此时他们共用了变量'[]'，在内存中指向同一个地址
4333551880
4333551880
而Charles因为传入了值，所以传入值覆盖了默认值，也就是charles的指针重新指向了['sword']
4333552776

结论：推荐参数arg默认值None  例如items=None 如下所示
使用判断语句is 判断None后赋予新的'[]' 每次都会在内存中开辟一个新的空间
"""


class Player(object):
    def __init__(self, name, items=None):
        self.name = name
        # if items is None:
        #     self.items = []
        # else:
        #     self.items = items
        self.items = items if items is not None else []
        print(id(self.items))


p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(p1.items)
print(p3.items)
