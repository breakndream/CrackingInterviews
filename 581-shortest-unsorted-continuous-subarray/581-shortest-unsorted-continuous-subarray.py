class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        if len(nums) <= 1:
            return 0
        
        while left < len(nums) - 1 and nums[left] <= nums[left+1] :
            left += 1
        
        while right > 0 and nums[right -1] <= nums[right] :
            right -= 1
            
        if left == len(nums) -1:
            return 0
        
        local_min = float("inf")
        local_max = - float("inf")
        
        for i in range(left, right+1) :
            local_min = min(local_min, nums[i])
            local_max = max(local_max, nums[i])
                
        while left > 0 and local_min < nums[left-1] :
            left -= 1
            
        while right < len(nums)-1 and local_max > nums[right+1]:
            right += 1
            
        
        return right - left + 1 