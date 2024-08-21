# -*- coding: utf-8 -*-
# @Time    : 2024/06/14
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py002_main_function_and_class\01_call_function.py
# @Desc    : 调用普通函数 和 类的函数

# import
def function01():
    print(f"this is function01.")

class MyClass:
    def __init__(self,name):
        self.name = name
    
    def callmyname(self):
        print("my name is:", self.name)

# main
if __name__ == '__main__':
    print( "main()." )
    # call function
    function01()
    # call class function
    myclass = MyClass("peng")
    myclass.callmyname()

	
    
