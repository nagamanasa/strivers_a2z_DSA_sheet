#https://takeuforward.org/data-structure/quick-sort-algorithm/

#O(n^2)
def partition(arr, low, high):
    pivot = arr[low]
    i = low+1
    j = high
    while (i<=j):
        if (arr[i]<=pivot):
            i+=1
        elif (arr[j]>=pivot):
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quick_sort(arr,low,high):
    if (len(arr)<=1):
        return arr
    if(low<high):
        partition_val = partition(arr,low,high)
        quick_sort(arr, low, partition_val-1)
        quick_sort(arr, partition_val+1, high)
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = quick_sort(arr, 0, len(arr)-1)
print(sorted_arr)