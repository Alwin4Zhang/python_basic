# -*- coding: utf-8 -*-
"""
  @CreateTime	:  2022/04/16 16:49:23
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
  
python定义：
只有最外层的for时立刻求值的，剩下的for或者if else等都是在生成器运行时再求值
"""

# list comprehensions 列表生成式

# lst = [1, 2, 3, 4, 5]
# # 第一个lst在generator构建时就使用了，第二个lst是在判断时使用的global invariable
# g = (i for i in lst if i in lst)  # 生成器
# lst = [0, 1, 2]
# print(id(g), list(g))

# # 上面的代码等价于下面的过程，lst1在g生成器时就已经使用了，if判断时才使用lst2
# lst1 = [1, 2, 3, 4, 5]
# g = (i for i in lst1 if i in lst2)
# lst2 = [0, 1, 2]
# print(list(g))

lst = [1, 2, 3, 4, 5]


def _g(it):
    for n in it:
        if n in lst:  # 当运行/使用生成器时才会去找全局的lst做判断
            yield n


# 建立生成器时直接使用到了lst，
g = _g(iter(lst))
lst = [0, 1, 2]
print(list(g))

lst = [1, 2, 3]
# for a in lst 在[1,2,3] generator创建时就用了  for b in lst中用的是generator使用时才用到lst=[1,2]
"""
等价于
for a in lst:
  for b in lst:
所以for a in lst是最外层的loop，只有它是在生成器生成时用到了，其他的内层的都是在生成器运行或者使用时才用到
"""
g = ((a, b) for a in lst for b in lst)
lst = [1, 2]
print(list(g))


"""
python在判断None的时候，一定记得要使用is None 或者 is Not None来判断

因为python的内置函数 例如 __bool__ 和 __eq__，当用户非法重载后，再判断None可能会出现问题
比如 a = None
if not a:    这个时候a=['{}',"",set(),0,None,False] 都满足if not a的条件
if a == None  在用户冲在了__eq__函数后可能会出现问题，并且 == 操作在底层代码中比 is 操作要慢，因为is
操作直接比较的是2个变量的指针地址
"""
