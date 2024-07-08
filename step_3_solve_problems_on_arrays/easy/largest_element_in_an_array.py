#https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/

def largest_element(arr):
    largest_number = arr[0]
    for i in arr:
        if largest_number<i:
            largest_number = i
    return largest_number
arr = [1,4,2,99,5,344]
print(largest_element(arr))