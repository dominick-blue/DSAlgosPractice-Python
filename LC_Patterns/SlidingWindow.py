'''

This is the Brute Force method to finding the average of contiguous subarrays of length "K"

Time & Space Complexity:

O(N*K) where "N" is the number of elements in an input array

'''

# def find_averages_of_subarrays(K,arr):
#     result = []

#     for i in range(len(arr)-K+1):
#         _sum = 0.0
#         for j in range(i, i+K):
#             _sum += arr[j]
#         result.append(_sum/K)
    
#     return result


'''

Optimized Approach

Time & Space Complexity:

O(N)

'''

def find_averages_of_subarrays(K,arr):
    result = []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K + 1:
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
