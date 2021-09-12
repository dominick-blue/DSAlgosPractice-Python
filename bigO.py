# This is an example of an O(n**2) function.
# The reason it is O(n**2) is because for n elements, the algorithm must iterate through both for loops.

def square(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)
square(4)