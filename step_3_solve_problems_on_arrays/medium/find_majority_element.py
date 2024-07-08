#https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/

def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = nums[0]
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif element == nums[i]:
                count +=1
            else:
                count-=1
        
        count = 0
        for i in range(len(nums)):
   
            if element == nums[i]:
                count +=1
        
        return element

nums = [3,2,3,2,3,111,9,3,3]
print(majorityElement(nums))