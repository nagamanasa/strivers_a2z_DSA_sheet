#https://takeuforward.org/data-structure/check-if-an-array-is-sorted/

def check_array(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i]<= arr[i+1]:
            count+=1
    if count == len(arr)-1:
        return True
    else:
        return False

arr = [11,2,4]
print(check_array(arr))