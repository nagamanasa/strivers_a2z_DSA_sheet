#https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/

def two_sum(nums,target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[nums[i]] = i

nums = [2,3,4,6,5]
target = 5
print(two_sum(nums,target))