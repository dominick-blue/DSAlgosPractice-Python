items = [20, 53, 84, 19, 56, 23, 87, 41, 6, 8]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # Recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # Now perform the merging

        i = 0 # index into the left array
        j = 0 # index into the right array
        k = 0 # index into the merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them

        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

print(items)
mergesort(items)
print(items)