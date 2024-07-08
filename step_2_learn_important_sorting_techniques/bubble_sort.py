#https://takeuforward.org/data-structure/bubble-sort-algorithm/

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j]  = temp
                swapped = True
        if swapped == False: #to avoid redundant swapping and jump out of the loop (because the arr is sorted)
            break
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
