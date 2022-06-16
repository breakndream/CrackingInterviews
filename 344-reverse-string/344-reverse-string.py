class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       
        length = len(s) 
        
        if length == 0 : 
            s = s
        elif length % 2 == 0:
            for i in range(length//2):
                temp = ""
                temp = s[i]
                s[i] = s[length - i - 1]
                s[length - i-1] = temp
            
        else :
        
            for i in range(length//2 + 1):
                temp = ""
                temp = s[i]
                s[i] = s[length - i - 1]
                s[length - i-1] = temp
                
        # nice to meet 
        
            
 
        
        # 0 , 5
        # 1, 4
        # 2, 3
        # length 6
        # !olleh
            
            