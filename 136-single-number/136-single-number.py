class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
     
        for key in count:
            if count[key] == 1 :
                return key
        

        