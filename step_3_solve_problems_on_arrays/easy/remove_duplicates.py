#https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/

def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = sorted(list(set(nums)))
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        return len(nums1)