#https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/

def hash1(arr, n):
    map = {}
    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    return map

arr = [1,4,2,10,5,10,15,10,5]
n = len(arr)
print(hash1(arr, n))