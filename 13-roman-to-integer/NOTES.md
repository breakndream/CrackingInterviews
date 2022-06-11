Tried 4 times.

교훈: 파이썬 dict 문법 dict = {"key":sth,
                              "value": sth,}
     string은 split 안해도 for loop 으로 iterate하면 char로 들어간다..
     저렇게 뒤에서부터 돌려야겠다는 생각은 어떻게 하는걸까..(사실 description에 힌트가 있다.
     Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV
     이 말은 특이 케이스의 경우 뒤에서부터 읽을 수도 있다는 걸로 
     
일단 python dictionary에 익숙하지않아서 작성법부터 애를 먹음.... array안에 dictionary object를 넣어줘야하나 고민했는데 그럴 필요가 없어서 처음부터 dict으로 갔다.
https://www.w3schools.com/python/ref_dictionary_values.asp ㅋㅋㅋㅋㅋ 이거보고 문법 참고함..(나 죽여)

1st Try
class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000                    
                   }  
        
        numbers = []
        value = 0
        length = len(s)
        
        for char in s:
            numbers.append(char)
        
        
        for i in range(length -1, -1, -1):
            
            if numerals[numbers[i]] < numerals[numbers[i-1]]:
                value +=  numerals[numbers[i]] - numerals[numbers[i-1]]
            else :
                value += numerals[numbers[i]]

       return value 
이럴 때의 문제점은 계산하고 나서도 numbers array 자체에는 아직 string이 남아있으니까 계산된게 다시 불려와서 계산 되는 문제점이 있었다.
예를 들어 print(romanToInt("LVIII"))    # 58 이렇게 나와야 되는데 III개가 계산되고 나서도 VI가 불려나와서 답이 다름..

2nd Try
class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000                    
                   }
       
        numbers = []
        value = 0
        length = len(s)
        
        for char in s:
            numbers.append(char)
            
        for i in range(length -1, -1, -1):
            
            if numerals[numbers[i]] < numerals[numbers[i-1]]:
                value +=  numerals[numbers[i]] - numerals[numbers[i-1]]
                numbers.pop(i)
                numbers.pop(i-1)
            else :
                value += numerals[numbers[i]]
                numbers.pop(i)
                
        return value 

그래서 이렇게 계산된건 pop을 해서 array에서 없앴는데 index out of range가 나오는 error 가 뜸
이유는 print(romanToInt("LVIII")) 이렇게 계산했을 때 L (index 0)이 다음 index를 찾기 때문

3rd Try 이때 string iterate되는데 왜 array를 만들어서 일을 키웠지.. 하면서 바꿈

class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000                    
                   }
        
        
        length = len(s)
        value = s[length-1]
        # string도 인덱스 됨..
        
        for i in range(length -2, -1, -1):
            
            if numerals[s[i]] < numerals[s[i+1]]:
                value -=  numerals[s[i]]
            else :
                value += numerals[s[i]]
                
        return value
        
 근데 TypeError: can only concatenate str (not "int") to str 이게 떠서 뭐야 하면서 고민하다가 안나와서 코드패스 답이랑 비교했음 
 
 문제는 line 94 였다.. ㅎㅎ 지금 value가 str임
 
 Final Try
 
 class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000                    
                   }
        
        
        length = len(s)
        value = numerals[s[length-1]]
        # string도 인덱스 됨..
        
        for i in range(length -2, -1, -1):
            
            if numerals[s[i]] < numerals[s[i+1]]:
                value -=  numerals[s[i]]
            else :
                value += numerals[s[i]]
                
        return value 
        
-End-
