class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # car ract -> anagram? no
        
        if len(s) != len(t):
            return False
        
        s_num = 0 
        s_item = dict()
        t_num = 0
        t_item = dict()
        
        for i in s:
            s_item[i] = s_item.get(i, 0) + 1
            s_num += ord(i)           
     
        for i in t:
            t_item[i] = t_item.get(i, 0) + 1
            t_num += ord(i)
            
        if s_num == t_num :
            if s_item == t_item:
                return True
            else:
                return False
        else :
            return False
            
            