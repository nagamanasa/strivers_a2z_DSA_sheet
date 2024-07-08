#https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/

def second_largest_element(arr):
    second_largest_element = arr[0]
    largest_element = max(arr)
    for i in arr:
        if i>second_largest_element and largest_element!=i:
            second_largest_element = i
    return second_largest_element
arr = [1,4,2,99,5,344]
print(second_largest_element(arr))