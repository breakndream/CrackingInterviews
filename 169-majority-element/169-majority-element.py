class Solution:
    def majorityElement(self, nums: List[int]) -> int:  
        
        length = len(nums) 
        if length == 0 :
            return 
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else :
                dict[i] += 1
                
        for key, value in dict.items():
            if value >= length/2 :
                return key
        return -1
          