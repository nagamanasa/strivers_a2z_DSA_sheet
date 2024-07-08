#https://takeuforward.org/data-structure/left-rotate-the-array-by-one/


def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n  # In case k is greater than the length of nums
    
    # Reverse the entire list
    nums.reverse()
    
    # Reverse the first k elements
    start, end = 0, k - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    
    # Reverse the remaining n - k elements
    start, end = k, n - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)
print(nums)
        