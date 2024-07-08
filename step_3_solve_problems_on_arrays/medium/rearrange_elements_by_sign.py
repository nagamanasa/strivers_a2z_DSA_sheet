#https://takeuforward.org/arrays/rearrange-array-elements-by-sign/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx = 0
        neg_idx = 1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos_idx] = nums[i]
                pos_idx += 2
            else:
                ans[neg_idx] = nums[i]
                neg_idx += 2
        return ans

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1, -2, -5, 2, -4]
    print(solution.rearrangeArray(nums))  # Output should be [3, -2, 1, -5, 2, -4]
