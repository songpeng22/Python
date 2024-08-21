# -*- coding: utf-8 -*-
# @Time    : 2024/08/15
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py005_array_list_operation\01_print_elements.py
# @Desc    : arry/list/set/tuple/dict
#          : list = []
#          : deque = deque()
#          : set = set()
#          : set = {1, 2, 3}
#          : tuple = () or 
#          : dict = {}

import string

# array
print(f"array example:")
import array as arr
array = arr.array("i", [3, 6, 9, 12])
print(f"type of array is:{type(array)}")
print(array)

import numpy as np
array_2 = np.array(["numbers", 3, 6, 9, 12])
print (array_2)
print(type(array_2))

# Lists
print(f"\nlist example:")
myList = [9, 'hello', 2, 'python']
print(f"type of myList is:{type(myList)}")
print(myList[0]) # output --> 9
print(myList[-3]) # output --> hello
print(myList[:2]) # output --> [9, 'hello']
print(myList) # output --> [9, 'hello', 2, 'python']
# quick list
newList = [1] * 3
print(f"newList:")
print(newList)
print(f"sum of list:{sum(newList)}")
# extend list
myList.extend(newList)
print(f"myList extend:")
print(myList)

testList = []
print(f"type of testList is:{type(testList)}")
# Adding Element into list
testList.append(5)
testList.append(10)
print("Adding 5 and 10 in list", testList)

# Popping Elements from list
testList.pop()
print("Popped one element from list", testList)
print()
# check is list
is_list = isinstance(testList,list)
print(f"is_list:{is_list}")

# deque
from collections import deque
# 创建一个空的deque
d = deque()
print(f"type of deque is:{type(d)}")
# 在deque的右侧添加元素
d.append(1)
d.append(2)
d.append(3)
print("deque:", d)  # 输出：deque([1, 2, 3])
d.pop()
print("deque:", d)  # 输出：deque([1, 2])

# Set
print(f"\nset example:")
s = set()
print(f"type of deqsetue is:{type(s)}")
what_01 = {1, 2, 3}
print(f"type of {{1, 2, 3}} is:{type(what_01)}")
what_02 = {1, 2, 3, "abc", 6}
print(f"type of {{1, 2, 3, 'abc', 6}} is:{type(what_02)}")
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)

# Tuple(元组)
print(f"\ntuple example:")
tuple_01 = ()
print(f"type of tuple is:{type(tuple_01)}")
t = tuple(testList)
print(f"type of tuple is:{type(t)}")
# Tuples are immutable
print("Tuple", t)

# tuple list(同时循环两个列表)
list_01 = [1,2,3]
list_02 = ["a","b","c"]
for (item_in_list1,item_in_list2) in zip(list_01,list_02):
    print(f"item_in_list1:{item_in_list1},item_in_list2:{item_in_list2}")

# Dictionary
print(f"\ndictionary example:")
d = {}
print(f"type of dict is:{type(d)}")

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)

#
font_list = ['Arial', 'Times New Roman', 'Verdana']
font_dict = {char: font_list[0] for char in string.ascii_uppercase + string.digits + "./年月日"}
font_dict['A'] = 'Times New Roman'
print(f"print all:")
print(font_dict)
font_dict['B'] = 'Verdana'
print(f"\nprint all:")
print(font_dict)
print("")
print(font_dict['B'])

# 其中多个key，快速赋值
print(f"\nassign values:")
font_dict_tmp = {char: 'Verdana' for char in "DEF"}
font_dict.update(font_dict_tmp)
print(font_dict)
