class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        pos = res = 0
        
        for i in reversed(columnTitle):
            digit = (ord(i) - 64)
            res += digit * 26**pos
            pos += 1

        return res
    
    # AB
    
        # A - Z
        # 1  - 26
        
        # AA - AZ
        # 27  - 52
        
        # AAA - AAZ
        # ABA - ABZ
        
        