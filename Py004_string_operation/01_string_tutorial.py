# -*- coding: utf-8 -*-
# @Time    : 2024/07/03
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py004_string_operation\01_string_tutorial.py
# @Desc    : string tutorial

import os
"""
"""

# string append - Concatenating string
print("Concatenating string:")
string = "hello"
str1 = string + "world"
print(str1)

# substring - check if conains substring
print("\ncheck if conains substring:")
fullstring = "StackAbuse"
substring = "tack"
if fullstring.find(substring) != -1:
    print("Found!")
else:
    print("Not found!")

# string replace
print("\nstring replace:")
string = "hello world"
print(f"string replace before:{string}")
string = string.replace("world","python")
print(f"string replace after:{string}")

# string split 
filename = "abc.jpg"
extension = filename.split('.')
print("\nextension list after split:")
print(extension)
print("\nextension is:")
print(extension[-1])

# split path
filename, file_extension = os.path.splitext('/path/to/somefile.ext')
print("\nfile name and extension:")
print(filename)
print(file_extension)