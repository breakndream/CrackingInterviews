class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(length) :
            j = i + 1
            for j in range(j, length):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        # for i in range(length):
        #     while i < j :
        #         if nums[i] + nums[j] != target:
        #             j-= 1
        #         else : 
        #             return [i, j]

        
