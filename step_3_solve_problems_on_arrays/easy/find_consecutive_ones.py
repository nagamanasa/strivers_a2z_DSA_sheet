#https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/

def cosecutive(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            count+=1
        else:
            count = 0
        max_count = max(max_count,count)
    return max_count
nums = [1,1,0,0,1,1,1,0,1,1,1,1,1]
print(cosecutive(nums))