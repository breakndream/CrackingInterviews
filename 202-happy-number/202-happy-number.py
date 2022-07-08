class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        
        while n not in visit:
            visit.add(n)
            n = self.sumofSquares(n)
        
        if n == 1:
            return True
        return False
        
    def sumofSquares(self, n) :
        calculation = sum(int(i)**2 for i in str(n))
        return calculation
        
        
        
        
        
        
        

# def is_Happy_num(n):
#   past = set()
#   while n != 1:
#         n = sum(int(i)**2 for i in str(n))
#         if n in past:
#             return False
#         past.add(n)
#   return True
# print(is_Happy_num(7))
# print(is_Happy_num(932))
# print(is_Happy_num(6))
            