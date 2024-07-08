#https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/


def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos] = nums[i]
            pos+=1
    
    while pos<len(nums):
        nums[pos] = 0
        pos+=1
    return nums

nums = [0,4,21,0,433]
nums = moveZeroes(nums)
print(nums)