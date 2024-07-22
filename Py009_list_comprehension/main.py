
vec = [-4, -2, 0, 2, 4]
print(f"original vec:")
print(vec)

# create a new list with the values doubled
doubled = [x*2 for x in vec]
print(f"doubled vec:")
print(doubled)
# [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
greater_thatn_0 = [x for x in vec if x >= 0]
print(f"greater_thatn_0 vec:")
print(greater_thatn_0)

# apply a function to all the elements
positive = [abs(x) for x in vec]
print(f"positive vec:")
print(positive)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruits_nospaces = [weapon.strip() for weapon in freshfruit]
print(f"striped:")
print(fruits_nospaces)
# output ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
squares = [(x, x**2) for x in range(6)]
print(f"(number, square):")
print(squares)
# output [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#
image_extensions = ['.jpg', '.jpeg', '.png']
files = ['0.txt','1.jpg', '2.jpeg', '3.png']
for file in files:
    if any(file.lower().endswith(ext) for ext in image_extensions):
        print(file)

