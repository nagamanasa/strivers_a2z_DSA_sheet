#https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/

def longest_subarray(arr,n,k):
    prefix_sum_map = {}
    sum = 0
    max_length = 0
    
    for i in range(n):
        # Update the prefix sum
        sum += arr[i]

        # Check if the prefix sum equals k
        if sum == k:
            max_length = i + 1  # From index 0 to i

        # Check if (sum - k) exists in the hashmap
        if (sum - k) in prefix_sum_map:
            # If it exists, it means there is a subarray with sum k
            max_length = max(max_length, i - prefix_sum_map[sum - k])

        # Store the first occurrence of each prefix sum
        if sum not in prefix_sum_map:
            prefix_sum_map[sum] = i
    
    return max_length

arr = [2,3,5,1,9]
n=5
k=10
print(longest_subarray(arr,n,k))