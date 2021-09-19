def linearSearch(list, item):
    index = 0
    found = False

    while index < len(list) and not found:
        if list[index] == item:
            found = True
        else:
            index += 1
    return found, item
list = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
print(linearSearch(list, 100))

