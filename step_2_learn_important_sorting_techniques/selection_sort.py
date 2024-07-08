#https://takeuforward.org/sorting/selection-sort-algorithm/

#O(n^2)
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i]  = temp
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = selection_sort(arr)
print(sorted_arr)