# array
print(f"array example:")
import array as arr
array_1 = arr.array("i", [3, 6, 9, 12])
print(array_1)
print(type(array_1))

import numpy as np
array_2 = np.array(["numbers", 3, 6, 9, 12])
print (array_2)
print(type(array_2))

# Lists
print(f"\nlist example:")
myList = [9, 'hello', 2, 'python']
print(myList[0]) # output --> 9
print(myList[-3]) # output --> hello
print(myList[:2]) # output --> [9, 'hello']
print(myList) # output --> [9, 'hello', 2, 'python']

testList = []
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

# Set
print(f"\nset example:")
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Tuple(元组)
print(f"\ntuple example:")
t = tuple(testList)

# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
print(f"\ndictionary example:")
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)