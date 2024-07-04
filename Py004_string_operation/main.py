import os
"""
"""

string = "hello"
# Concatenating string
print("Concatenating string:")
str1 = string + "world"
print(str1)

# check if conains substring
print("\ncheck if conains substring:")
fullstring = "StackAbuse"
substring = "tack"

if fullstring.find(substring) != -1:
    print("Found!")
else:
    print("Not found!")

# split string
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