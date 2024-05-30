#https://takeuforward.org/data-structure/reverse-a-given-array/

def reverse_array(arr, start, end):

    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse_array (arr, start+1, end-1)
    return arr

arr = reverse_array([1,2,3,4],0, 3)
print(arr)