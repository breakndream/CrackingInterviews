class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        new_string = ""
        
        for i in s.split():
            stack.append(i.strip())
        
        while stack:
            new_string += stack.pop() + " "
            
        return new_string[:len(new_string)-1]
            
        
            