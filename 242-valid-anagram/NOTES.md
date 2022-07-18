### 1st Try

   def isAnagram(self, s: str, t: str) -> bool:
        # car ract -> anagram? no
        
        if len(s) != len(t):
            return False
        
        s_num = 0 
        s_set = set(s)
        
        for i in s:
            s_num += ord(i)
            
        t_num = 0
        t_set = set(t)
        
        for i in t:
            t_num += ord(i)
        
        if s_num == t_num :
            diff = s_set - t_set
            if diff:
                return False 
            else:
                return True
        else :
            return False
            
Edge Case : "acacbac" / "bbbbbac" -> set으로 안 되길래 걍 dictionary로 바꿔서 했다.

##  s_item[i] = s_item.get(i, 0) + 1 : adding items into a dictionary one liner!!!
