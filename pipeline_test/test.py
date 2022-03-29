# -*- coding: utf-8 -*-
'''
    @Time    : 2022/3/27 7:14 PM
    @Author  : alwin
    @Email   : alwin114@hotmail.com
'''


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def create(cls, name, age):
        return cls(name, age)


print(Person)
p = Person(name='zs', age=18)
print(p)

print(Person.create(name='zs', age=18))
