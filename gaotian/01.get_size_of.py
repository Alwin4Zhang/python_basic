# -*- coding: utf-8 -*-
"""
  @CreateTime	:  2022/04/16 11:16:57
  @Author	:  Alwin Zhang
  @Mail	:  zjfeng@homaytech.com
"""
"""
三个看似一样的列表，占用内存空间竟然不一样多

python3中一个list在内存中空间是 56
一个指针占用空间是 8

[0] * 3  占用  56 + 8 * 3 = 80
[0 for _ in range(3)]  56  + 4 * 8 = 88
"""

import sys

print(sys.getsizeof([0] * 3))
print(sys.getsizeof([0, 0, 0]))
print(sys.getsizeof([0 for _ in range(3)]))
