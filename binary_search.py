def binarySearch(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found, item

list = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
list.sort()

print(binarySearch([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 12))