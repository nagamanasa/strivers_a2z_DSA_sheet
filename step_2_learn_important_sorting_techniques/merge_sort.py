#https://takeuforward.org/data-structure/merge-sort-algorithm/

#O(n log n)
def merge_sort(arr,left,right):
    if (left>=right):
        return arr
    mid = (left+right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge (arr, left, mid, right)
    return arr

def merge(arr, left, mid, right):
    temp = []
    l = left
    r = mid+1
    while (l<=mid and r<=right):
        if (arr[l] <= arr[r]):
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    
    while (l<=mid):
        temp.append(arr[l])
        l+=1
    
    while (r<=right):
        temp.append(arr[r])
        r+=1

    for i in range(len(temp)):
        arr[left+i] = temp[i]

arr = [13,46,24,52,20,9]
sorted_arr = merge_sort(arr,0,len(arr)-1)
print(sorted_arr)

