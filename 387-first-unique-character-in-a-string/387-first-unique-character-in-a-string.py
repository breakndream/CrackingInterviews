class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        new_dict = {}
        
        for i in range(len(s)):
            if s[i] in new_dict:
                new_dict[s[i]] = None 
            else :
                new_dict[s[i]] = i
        
        print(new_dict)
        
        for key in new_dict:
            if new_dict[key] is not None:
                return new_dict[key]
            else:
                continue
        return -1
                
            