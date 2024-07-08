#https://takeuforward.org/data-structure/insertion-sort-algorithm/

#O(n^2)
def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while (j > 0 and arr[j-1] > arr[j]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1]  = temp
            j-=1
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
