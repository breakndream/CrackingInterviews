class Solution:
    def myAtoi(self, s: str) -> int:
        
        s, res = s.strip(), ''
        
        if s == '': return 0
        
        elif s[0] == '-': 
            res += '-'
            s = s[1:]
            
        elif s[0] == '+': 
            res += '+'
            s = s[1:]
            
        for dig in s:
            if dig.isnumeric(): res += dig
            else: break
                
        res = '0' if res in ['+','-',''] else res
        
        return max(int(res), - (2**31)) if int(res) < 0 else min(int(res), (2**31 - 1))
    
#         neg = False
#         res = 0 
#         new_string = ""
#         s = s.strip()
        
#         if not s : return 0
        
#         for i in range(len(s)):
#             if s[i] == "+" or s[i] == "-":
#                 continue
#             elif s[i] == ".":
#                 continue
#             else :
#                 if not (ord(s[i]) >= 48 and ord(s[i]) <= 57):
#                     return 0 
 
#         for i in s:
#             if i == "-" :
#                 neg = True
#                 continue
#             if i == ".":
#                 break
#             if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 45 :
#                 new_string += i 

#         digit = len(new_string) -1
        
#         for i in new_string:
#             res += 10 ** digit * (ord(i) - 48) 
#             digit -= 1
        
#         if neg :
#             res = -1 * res

#         pos_limit = 2147483647
#         neg_limit = -2147483648
        
#         if res > pos_limit :
#             return pos_limit
#         if res < neg_limit:
#             return neg_limit
#         else :
#             return res
            