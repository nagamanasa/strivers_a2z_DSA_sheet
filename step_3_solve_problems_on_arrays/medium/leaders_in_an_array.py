#https://takeuforward.org/data-structure/leaders-in-an-array/

class Solution:
    # Back-end complete function Template for Python 3
    
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        max_ele = arr[-1]
        arr1 = [max_ele]  # Start with the last element which is always a leader
        for i in range(n-2, -1, -1):  # Traverse the array from right to left
            if arr[i] >= max_ele:
                max_ele = arr[i]
                arr1.append(arr[i])
        return arr1[::-1]  # Reverse to maintain the order of leaders

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 6
    arr = [6, 5, 4, 3, 2, 1]
    print(solution.leaders(n, arr))  # Output should be [6, 5, 4, 3, 2, 1]
