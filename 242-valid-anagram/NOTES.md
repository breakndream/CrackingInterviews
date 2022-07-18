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
그리고 어떻게 s_num 이랑 t_num 이랑 traverse 할 지.. O(n^2) 니까.. 생각을 많이 했는데 그냥 == 쓰면 될 것 같아서 썼는데 됐다.. 
어쨌든 저것도 time complexity 가 좋진 않을 듯

##  s_item[i] = s_item.get(i, 0) + 1 : adding items into a dictionary one liner!!!
