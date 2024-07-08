#https://takeuforward.org/arrays/recursive-insertion-sort-algorithm/

#O(n^2)

def recursive_insertion_sort(arr, i, len):
    if (i == len):
        return arr
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp
        j-=1

    recursive_insertion_sort(arr, i+1, len)
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = recursive_insertion_sort(arr, 0, len(arr))
print(sorted_arr)
