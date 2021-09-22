items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        left_index = 0
        right_index = 0
        merged_index = 0

        while left_index < len(leftarr) and right_index < len(rightarr):
            if leftarr[left_index] < rightarr[right_index]:
                dataset[merged_index] = leftarr[left_index]
                left_index += 1
            else:
                dataset[merged_index] = rightarr[right_index]
                right_index += 1
            merged_index += 1


        while left_index < len(leftarr):
            dataset[merged_index] = leftarr[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(rightarr):
            dataset[merged_index] = rightarr[right_index]
            right_index += 1
            merged_index += 1

print(items)
mergesort(items)
print(items)
