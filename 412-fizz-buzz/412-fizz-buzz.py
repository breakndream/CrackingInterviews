class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # make a list: length n
        # iterate values in the list
        # if i % 15 == 0 부터 시작
        #len(list) = 15 이렇게는 못함
        
        list = []
        
        for i in range(1, n+1):
            if i % 15 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0 :
                list.append("Buzz")
            else:
                i = str(i)
                list.append(i)
        
        return list
                
        