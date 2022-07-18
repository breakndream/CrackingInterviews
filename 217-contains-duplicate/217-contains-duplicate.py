class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        unique = dict()
        
        for i in range(len(nums)) :
            if nums[i] in unique :
                return True
            else:
                unique[nums[i]] = 1
        return False
            
        