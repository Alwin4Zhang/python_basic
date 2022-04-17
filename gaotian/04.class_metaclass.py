# -*- coding: utf-8 -*-
"""
  @CreateTime	:  2022/04/16 21:23:12
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
"""
from pprint import pprint


class A(object):
    name = "zhangsan"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def k(self, a):
        print(a)


a = A("zhangsan", 20)

# print(a.__dict__)
# print(vars(a))
# print(dir(a))

# 获取所有成员变量
# pprint(A.__dict__)

"""
使用type创建类
"""


# def f(self):
#     print(1)


# d = {"name": "AAA", "f": f}
# A = type("A", (), d)

# a = A()
# pprint(A.__dict__)

# ------------------------------------------------------------------------------------------------------------------------------
import random


class M(type):
    def __new__(cls, name, bases, dict):
        print(name, bases, dict)
        return type.__new__(cls, name, bases, dict)

    def __init__(self, name, bases, dict):
        print(name, bases, dict)
        self.random_id = random.randint(0, 100)
        return type.__init__(self, name, bases, dict)

    def __call__(cls, *args, **kwargs):  # 在创建metaclass的子类的实例时被调用
        print("call")
        return type.__call__(cls, *args, **kwargs)


class B(metaclass=M):
    pass


b = B()
# print(b.random_id)
