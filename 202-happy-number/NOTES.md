### 눈물 나는 Recursion 도전기


1st Try:

 class Solution:
     def isHappy(self, n: int) -> bool:
        calculation = 0

        numList = [int(n) for n in str(n)]

        
        while len(numList) > 1 :
            number = numList.pop()
            number = number * number
            calculation += number
        
        
        if len(numList) == 1:
            if numList[0] == 1:
                return True
            else :
                return False
        else:
            self.isHappy(calculation)
            
2nd Try :

class Solution:
    def isHappy(self, n: int) -> bool:
        
        calculation = 0

        numList = [int(n) for n in str(n)]
        
        while len(numList) > 0 :
            number = numList.pop()
            number = number **2
            calculation += number

        if calculation == 1:
            return True
        else:
            self.isHappy(calculation)
 
3rd Try :

class Solution:
    
    cycle = 999
    
    def isHappy(self, n: int) -> bool:
        
        
        return Solution.calculate(n)

    def calculate (n): 
        
        calculation = 0
        
        numList = [int(n) for n in str(n)]

        while len(numList) > 0 :
            number = numList.pop()
            number = number **2
            calculation += number

        if calculation == 1:
            return True
        else:
            if cycle > 0 :
                Solution.calculate(calculation)
                cycle -= 1
            else :
                return False
 
 여기서 recursion 으로 회생 불가함을 나연이와 발견.. 눈물을 머금고 포기 ㅋ....
 NeetCode 풀고 set()으로 다시 풀었다. LinkedList Cycle로 풀고 싶어서 다른 문제 도전
