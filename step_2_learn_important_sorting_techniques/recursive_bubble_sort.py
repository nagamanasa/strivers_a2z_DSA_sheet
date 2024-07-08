#https://takeuforward.org/arrays/recursive-bubble-sort-algorithm/

#O(n^2)

def recursive_bubble_sort(arr, len):
    if (len == 1):
        return arr
    for i in range(len-1):
        if arr[i] >= arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    recursive_bubble_sort(arr, len-1)
        
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = recursive_bubble_sort(arr, len(arr))
print(sorted_arr)