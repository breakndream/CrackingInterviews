class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closingTag = {")": "(", "}":"{","]":"["}
       
        
        for paren in s :
            if paren in closingTag:
                if stack and stack[-1] == closingTag[paren]:
                    stack.pop()
                else : 
                    return False
            else:
                stack.append(paren)
        return True if len(stack)== 0 else False
                
                
                
        # "()[]{}"
        #({[]})