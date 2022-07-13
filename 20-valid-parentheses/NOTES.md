**1st Try: {([])}-> 이렇게 되는 경우만 따짐: 해커랭크에서**

    def isValid(self, s: str) -> bool:
        length = len(s)
        stack = []
        queue = []
        if length == 0 :
            return True
        elif length % 2 != 0 :
            return False
        else :
            for i in range(length//2):
                if s[i] == "{":
                    a = "}"
                elif s[i] == "[":
                    a = "]"
                elif s[i] == "(" :
                    a = ")"
                queue.append(a)
            
            for i in range(length//2,length):
                stack.append(s[i])
            
            while len(queue) > 0:
                a = queue.pop(0)
                b = stack.pop()
                if a == b:
                    continue
                else :
                    return False
            return True
            
**2nd Try: 알고보니 ()[]{}도 되는 것이었다 -> NeetCode 봄**

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
        return True 
        
 Edge Case : ["(", "("] 이 경우 해결 못 함..
 
 그래서 stack 이 empty일 때라는 조건을 넣어줘야 

