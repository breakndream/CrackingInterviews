class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        print(n)
        while n:
            res += n % 2
            n = n >> 1
        return res
    
#         n = format(n,'b')
#         counter = 0 
#         for i in str(n):
            
#             if i == '1':
#                 counter += 1
#             else:
#                 continue

#         return counter

