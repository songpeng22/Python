def my_function01(*args):
    print(args)
    print(args[0])

def my_function02(*args):
    print(f"args[0]:{args[0]}")
    print(f"args[1]:{args[1]}")
    for it in args:
        print(it)

print(f"my_function01:")
my_function01(1, 2, 3)  
# 输出: (1, 2, 3)
print(f"\nmy_function02:")
my_function02(1, 2, 3)  
# 输出：
# 1
# 2
# 3

# create an *args
print(f"\nmy_function02:")
myList = []
myList.append("/path/a")
myList.append("/path/b")
myList.append("/path/c")
my_function02(*myList)

print(f"\nmy_function02:")
my_function02(*[4,5,6])  
