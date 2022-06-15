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
        
        numbers= []
        length = len(s)
    
        for char in s:
            numbers.append(char)
        
        value = numerals[numbers[length-1]]
        
        
        for i in range(length -2, -1, -1):
            
            if numerals[numbers[i]] < numerals[numbers[i+1]]:
                value -=  numerals[numbers[i]]
            else :
                value += numerals[numbers[i]]
                
        return value 

            