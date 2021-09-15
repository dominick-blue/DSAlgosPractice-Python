import sys


def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    left = A[first:middle+1]
    right = A[middle+1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 0
    for k in range(first, last + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


A = [5,9,1,2,4,8,6,3,7]
print(A)
merge_sort(A)
print(A)
