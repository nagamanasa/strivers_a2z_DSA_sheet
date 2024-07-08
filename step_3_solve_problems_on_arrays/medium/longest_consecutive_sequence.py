#https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This method finds the longest consecutive sequence in an array of numbers.
        
        :param nums: List of integers
        :return: The length of the longest consecutive elements sequence
        """
        # Convert the list to a set to remove duplicates and allow O(1) lookups
        nums_set = set(nums)
        max_count = 0
        
        # Iterate through each number in the set
        for num in nums_set:
            # Check if it's the start of a new sequence
            if num - 1 not in nums_set:  # Start of a new sequence
                current_num = num
                count = 1  # Initialize count for this sequence
                
                # Count all consecutive numbers following num
                while current_num + 1 in nums_set:
                    current_num += 1
                    count += 1
                
                # Update max_count if the current count is greater
                max_count = max(max_count, count)
                
        return max_count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    test_nums = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive sequence length:", solution.longestConsecutive(test_nums))
