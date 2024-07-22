#The any() function returns the boolean value:
#True if at least one element of an iterable is true
#False if all elements are false or if an iterable is empty

mylist = [False, True, False]
x = any(mylist)
print(f"x: is any element true?:{x}")

mylist = [False, 0, False]
x = any(mylist)
print(f"x: is any element true?:{x}")