## 미친놈 문제...

아니 처음에 codepath에서 한대로 하려다가 edge case 너무 많아서 오류가 계속 났다.
배운 ord()나 chr() 로 아스키 코드 변환해서 풀려고 그랬는데 걍 안되는 것 같아서 나중에는 답 복붙함

근데 복붙한 isnumeric 도 쓰고 쉽게 쉽게 가서...흠....

    def myAtoi(self, s: str) -> int:
        neg = False
        res = 0 
        new_string = ""
        s = s.strip()
        
        if not s : return 0
        
        for i in range(len(s)):
            if s[i] == "+" or s[i] == "-":
                continue
            elif s[i] == ".":
                continue
            else :
                if not (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                    return 0 
 
        for i in s:
            if i == "-" :
                neg = True
                continue
            if i == ".":
                break
            if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 45 :
                new_string += i 

        digit = len(new_string) -1
        
        for i in new_string:
            res += 10 ** digit * (ord(i) - 48) 
            digit -= 1
        
        if neg :
            res = -1 * res

        pos_limit = 2147483647
        neg_limit = -2147483648
        
        if res > pos_limit :
            return pos_limit
        if res < neg_limit:
            return neg_limit
        else :
            return res
            
