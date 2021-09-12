# The purpose of this file is to document practice of data structures within the Python 3 language

# Pythons Built-In Data structures

# Sequence Types: We can access elements within these types with indexing

# Strings

# Indexing
x = 'frog'
# print(x[0]) # Gives us 'f'

# Slicing
x = 'Computer'
comp = x[:4].lower()
cpe = x[::3].lower()

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 9]

set(a).intersection(set(b))

# print(x[1:4]) # Starts at the 'o'. Start is inclusive and End is Non-inclusive
# print(x[1:6:2]) # Retrieves every SECOND step or element
# print(x[3:])
# print(x[:5])
# print(x[-1])
# print(x[-3:])
# print(x[:-2])
# print(cpe)


# print('x' in x)

# lists

# Adding and Concatenating

y = ['cow', 'chicken', 'horse', 'car']
# print('cow' not in y) # A way of checking membership

# Iterating through the items in a sequence

# for index, item in enumerate(y):
#     print(index, item)

xy = [y[1]] + ['house', 'airplane']

num_list = [9, 10, 11, 2, 3]
num_list
print(num_list)

# print(xy)
# tuples # Biggest difference between tuples and lists are that tuples are immutable and lists are mutable
# tuples are faster than lists

z = ('Dominick', 'Jasmine', 'Beverly', 'Diana')
# print(min(z)) # For strings will print the alpha-numerically smallest element ('Beverly' is the first element)



zy = z + ('JaeLynn',)

zy = zy * 3
# print(zy)
# sets



# General
# queues
# stacks
# heaps
# linked lists

# Algos

# binary search trees
