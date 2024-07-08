#https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/

def singleNumber(self, arr: list[int]) -> int:
        hashmap = {}
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for i in range(len(arr)):
            if hashmap[arr[i]]==1:
                return arr[i]

arr = [2,2,4,2,1,1,3]
print(singleNumber(arr))
