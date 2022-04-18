# -*- coding: utf-8 -*-
'''
  @CreateTime	:  2022/04/18 21:15:48
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
'''


# 无法访问类或对象的数据，所以可以把它当做一个辅助功能方法用，里面包含一些与该类有关的逻辑代码，比如validate(*args)
# classmethod可以设置修改类属性，也可以实例化对象
"""
classmethod 必须有一个cls object作为paramether
staticmethod 可以没有参数

classmethod的优势:
1.我们已经在一个地方实现了日期字符串解析，现在它可以重用了
2.封装在这里工作得很好（如果您认为可以在其他地方将字符串解析实现为单个函数，则此解决方案更适合 OOP 范式）
3.cls 是一个包含类本身的对象，而不是类的实例。这很酷，因为如果我们继承我们的 Date 类，所有的孩子也将定义 from_string

staticmethod:
所以，正如我们从staticmethod的使用中所看到的，我们没有任何访问类是什么的权限---它基本上只是一个函数，在语法上像方法一样被调用，但没有访问对象及其内部（字段和其他方法）的权限，而classmethod有。
"""


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        data1 = cls(day, month, year)
        return data1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string("11-09-2012")
is_date = Date.is_date_valid('11-09-2012')


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return "{0}-{1}-{2}".format(self.month, self.day, self.year)

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)

    @classmethod
    def mill(cls, month, day):  # 类方法，可以被子类继承
        return cls(month, day, 2000)


new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1)  # also creates a Date object.

# Proof:
print(new_year.display())           # "1-1-2013"
print(millenium_new_year.display())  # "1-1-2000"

isinstance(new_year, Date)  # True
isinstance(millenium_new_year, Date)  # True


class DateTime(Date):
    def display(self):
        return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)


datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)
datetime3 = DateTime.mill(10, 10)

isinstance(datetime1, DateTime)  # True
isinstance(datetime2, DateTime)  # False

print(datetime1.display())  # returns "10-10-1990 - 00:00:00PM"
# returns "10-10-2000" because it's not a DateTime object but a Date object. Check the implementation of the millenium method on the Date class for more details.
print(datetime2.display())
print(datetime3.display())
