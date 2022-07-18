class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        
        while 0 in nums:
            nums.remove(0)
            counter += 1
                
        while counter:
            nums.append(0)
            counter -=1
            
        return nums