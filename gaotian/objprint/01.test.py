from objprint import objprint, add_objprint

# from objprint import install

# install()


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player:
    def __init__(self):
        self.name = "Alice"
        self.age = 18
        self.items = ["axe", "armor"]
        self.coins = {"gold": 1, "silver": 33, "bronze": 57}
        self.position = Position(3, 5)
        self.person = Person("zhangsan", 18)


# @add_objprint
# class Player:
#     def __init__(self):
#         self.name = "Alice"
#         self.age = 18
#         self.items = ["axe", "armor"]
#         self.coins = {"gold": 1, "silver": 33, "bronze": 57}
#         self.position = Position(3, 5)


# objprint(Player())

# This will print the same thing as above
# print(Player())


# If you want the str representation of the object, instead of printing it on the screen, you can use objstr function
# from objprint import objstr

# s = objstr(Player())
# print(s)


"""
print the method signature without self argument
"""
from objprint import op


# class Player:
#     def attack(self, opponent):
#         pass


# op(Player(), print_methods=True)

# line numbers
# def f():
#     op(Player(), line_number=True)
# f()

from objprint import objjson
import json

json_obj = objjson(Player())

# print(json.dumps(json_obj, indent=2))

# op(Player(), format="json", indent=2)

# 装饰器模式
# @add_objprint(format='json',indent=2)
# class Player:
#     pass

# print(Player())

# 指定输出的字段
# op(Player(), include=["name", "coins"])

# 正则匹配输出字段  排除包括满足正则条件的变量 re.fullmatch(patten,key)
op(Player(), exclude=[".*n"])

"""
install方式使用
"""
# from objprint import op, install

# # Now you can use op() in any file
# install()

# # This is the same
# op.install()

# # You can specify a name for objprint()
# install("my_print")
# my_print(Player())
