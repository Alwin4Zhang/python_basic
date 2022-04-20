# -*- coding: utf-8 -*-
'''
  @CreateTime	:  2022/04/20 20:54:56
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
'''

from typing import Dict

"""
1.关于_share_state:
在__init__(self,)外面定义的变量，是属于这个class的，并且由所有的instance共享的，而不是单属于某个instance；
在__init__(self,)里面定义的变量，只属于这个object instance(self)本身
2.关于__dict__:
类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类的__dict__里面的，对象的__dict__中存储了一类
self.xxx的一些东西

Borg模式是单例模式在python中的变种。传统单例模式在python中，存在继承兄弟类之间状态隔离的问题。
Borg模式将全部实例，与子类的全部实例。共用同一个__dict__。这样保证了所有实例状态的一致性。同样属于单例模式的理念
"""


class Borg:
    _share_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._share_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:  # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"
            print(self.__dict__)

    def __str__(self):
        return self.state


def main():
    rm1 = YourBorg()
    rm2 = YourBorg()

    rm1.state = "Idle"
    rm2.state = "Running"
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))


if __name__ == "__main__":
    main()
