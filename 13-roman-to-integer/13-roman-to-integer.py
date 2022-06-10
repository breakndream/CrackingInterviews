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

            