​1st Try 에 해결 되었긴하나 이미 파이썬으로도 자바스크립트로도 풀어본 것 ㅋ  
교훈 : 늘 주어진 제시문 잘 읽기 -> 처음에는 Array의 element들이 string으로 나와야 한다는 걸 몰랐음

1. length 가 n인 empty list를 만들어주고 iterate 하면서 value를 바꿔주려고 했음

list = []
len(list) = 15 이렇게 하려고 했는데 안됐다
https://stackoverflow.com/questions/10712002/create-an-empty-list-with-certain-size-in-python

2. 근데 그냥 iterate하면서 correspond value를 append 해주면 되는 거였음!
1st Try

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
    
        list = []
        
        for i in range(n):
            if i % 15 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0 :
                list.append("Buzz")
            else:
                list.append(i)
        
        return list
 
 근데 list element 들이 다 str 그리고 1부터 시작해야함.
 https://www.w3schools.com/python/ref_func_str.asp -> str() 쓰면 해결 된다는 걸 알음 早くpythonの文法に慣れて！！！
 
 2nd Try
 
 class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
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
 
 -End-
 
                
