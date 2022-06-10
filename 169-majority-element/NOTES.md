코드패스에서 문제 나와서 친구들 거 참조하면서 품

교훈 indentation 주의하자 / dictionary syntax 공부하기
https://www.w3schools.com/python/python_dictionaries_loop.asp -> loop syntax

dictionary syntax 모르는 건 repl.it 에서 해결

leetcode에서 1st Try

    def majorityElement(self, nums: List[int]) -> int:  
        
        length = len(nums) 
        if length == 0 :
            return 
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else :
                dict[i] += 1
        for key, value in dict.items():
            if value > length/2 :
                return key
            return -1
     
이 경우 input이 [6,5,5]이면 key가 6때 else statement 즉 return -1로 가서 key 5의 value 2가 아니라 -1이 나와서 오답이다.
indentation의 중요성

그래서 정답은
    def majorityElement(self, nums: List[int]) -> int:  
        
        length = len(nums) 
        if length == 0 :
            return 
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else :
                dict[i] += 1
        for key, value in dict.items():
            if value > length/2 :
                return key
        return -1

