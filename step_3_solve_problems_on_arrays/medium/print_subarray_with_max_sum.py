#https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

import sys
def maxSubArray(nums: list[int]) -> int:
    sum_local = 0
    max_sum = -sys.maxsize
    start_idx = 0
    temp_start = 0
    end_idx = 0
    
    for i in range(len(nums)):
        sum_local += nums[i]

        if sum_local > max_sum:
            max_sum = sum_local
            start_idx = temp_start
            end_idx = i

        if sum_local < 0:
            sum_local = 0
            temp_start = i + 1

    print(f"The subarray with the maximum sum is: {nums[start_idx:end_idx+1]}")
    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum is {maxSubArray(arr)}")