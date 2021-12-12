#  Brute Force approach

def find_averages_of_subarrays(K,arr):

    result = []

    for i in range(len(arr)-K+1):
        total = 0.0
        for j in range(i, i+K):
            total += arr[j]
        result.append(total/K)
    
    return result



def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
