#https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/


def maxSubArray(self, nums: list[int]) -> int:
    sum_local = 0
    max_sum = -inf
    for i in range(len(nums)):
        sum_local += nums[i]

        if sum_local > max_sum:
            max_sum = sum_local

        if sum_local<0:
            sum_local = 0
    return max_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(arr))