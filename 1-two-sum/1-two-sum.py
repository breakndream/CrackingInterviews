class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(length) :
        #     j = i + 1
        #     for j in range(j, length):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        j = len(nums) - 1
        for i in range(len(nums)):
            
            while i < j :
                if nums[i] + nums[j] == target:
                    return [i, j]
                j-= 1

            j = len(nums) -1

        
