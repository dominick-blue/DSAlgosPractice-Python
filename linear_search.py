# def linearSearch(dlist, item):
#     index = 0
#     found = False
#
#     while index < len(dlist) and not found:
#         if dlist[index] == item:
#             found = True
#         else:
#             index += 1
#
#     return found, index
#
# dlist = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
# print(linearSearch(dlist, 56))

# def linearSearch(list, item):
#     index = 0
#     found = False
#
#     while index < len(list) and not found:
#         if list[index] == item:
#             found = True
#         else:
#             index += 1
#
#     return found, item
#
# dlist = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
# print(linearSearch(dlist, 56))

def linearSearch(list, item):
    index = 0
    found = False

    while index < len(list) and not found:
        if list[index] == item:
            found = True
        else:
            index += 1
    return found, item
dlist = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
print(linearSearch(dlist, 56))

