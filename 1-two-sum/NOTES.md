1시간 소요

1st Try 문제 자체를 not fully understand 

 def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(target):
            if nums[i] + nums [i+1] == target:
                return [i, i+1]

그냥 nums[i] 랑 nums[i+1]만 하면 되는 줄 알았는데 index out of bound 에러가 계속 났음.. 당연함;;
만약에 input array가 [3,2,3] 이면 마지막 index 2일 때 3으로 넘어가니까 

2nd Try   사실 중간에 한 번 트라이가 더 있긴 함.

def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(1, length):
            if nums[i-1] + nums [i] == target:
                return [i-1, i]   

range에 bound를 주면 (range(1,5)이면 1~4까지 돌음) upper bound -1 까지인 걸 생각하고 ragne (1, length-1)을 햇었는데 
이미 length 자체가 len() method써서 index +1 되어있는 상태여서 할 필요가 없었음 -> 유념할 것

쨌든 고치고 다시 푸니 에러가 났음 
Input: [3,2,3] 6 output: [] Expected: [0,2] 이 경우도 있었던 거임
Example들에 안나와있어서 생각도 못했는데 understand 때 시간을 좀 더 써봐야 할 듯.. edge case 생각하고

3rd Try 다시 난관 봉착.. 그래서 어떻게 할 것인가 
For loop 두 개 쓰는 거는 time complexity 에서 똥망이고..hash map 사용해서 key value로 저장한 다음 새로운 array만들어서 그걸 sort해버릴까 생각도 해봤는데 
흠 sort되어도 두개 같이 붙어있어야 한다는 보장이 없음 만약에 target 이 11인데 [1,2,3,4,5,7] 이면 4,7 더하면 return 값이 있어야 하니까..
그래서 구상한 건 pointer 두개 나눠서 startPoint는 increment하고 endPoint는 decrement 하려고 했음.

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        endPoint = len(nums)-1
        startPoint = 0
        while startPoint < endPoint:
            if nums[startPoint] + nums [endPoint] == target:
                return [startPoint, endPoint]
            else :
                endPoint-=1
                continue
 근데 문제는 여기서 startPoint가 increment가 안됨.. 
 
 def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        startPoint = 0
        endPoint = len(nums)-1
        
        while startPoint < endPoint:
            #if nums[startPoint] > target:
                #startPoint += 1
            if nums[startPoint] + nums [endPoint] == target:
                return [startPoint, endPoint]
            else :
                endPoint-= 1
                
   def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        j = length - 1
        
        for i in range(length):
            while i < j :
                if nums[i] + nums[j] != target:
                    j-= 1
                    continue
                else : 
                    return [i, j]
그래서 while loop 에 나간 다음에 다시 for loop 으로 돌아가서 increment하게 해주려고 난리를 쳤는데 안됨.. -> 이부분 물어보기 

4th Try 그래서 써치하다가 stack overflow 에서 스포 당해서 걍 아 와 뒤에서 부터 decrement할 생각을 했지..? 와 for loop 두개 다 쓰길래 걍 나도 ㅇㅋ 쓰기루 함

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        j = length - 1
        
        for i in range(length) :
            for j in range(length):
                if nums[i] + nums[j] == target:
                    return [i,j]
이렇게 했는데 이 경우 j가 내가 생각하던 것 처럼 i 다음부터 시작하는게 아니라 j 도 length 가 5면 0~4 까지 돌아가서 
Input: [3,2,4] 6  Output: [0,0] 이런 불상사 발생..

Final : 그래서 이렇게 했다고 한다
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(length) :
            j = i + 1
            for j in range(j, length):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    
교훈 : understand 단계에서 edge case 도 생각해보고 이해 정확하게 했나 생각해보기 
index out of bound같은 기초 에러는 안나게 하기. 계속 돌려보지말고 신중하게!! for loop startPoint increment 되는 거 왜 안되는지.... 물어보기 

---

나연이랑 two pointer로 해결!
문제는 [1,2,3,4,5] target = 7 일 떄 output 이 [2,3]니 나와야 함. 나혼자 풀었을 때의 문제는 line 108번이 없어서 j를 업데이트 안해줬다는 거. 
(업데이트를 안해주면 i가 0일때 j가 1까지 가고 그다음 i를 increment했을 때도 while loop 안으로 안들어감)
 j = len(nums) - 1
        for i in range(len(nums)):
            
            while i < j :
                if nums[i] + nums[j] == target:
                    return [i, j]
                j-= 1

            j = len(nums) -1

---
1)
  if nums[i] + nums[j] != target:
       j -= 1
    return [i, j]

2)
    if nums[i] + nums[j] == target:
       return [i, j]
    j -= 1

1은 return 이 else 일 때가 아니라 flow 상 if 안에 들어갔다가 무조건 실행됨.
그래서 이번 문제의 경우 2) 로 적어줘야함. 아니면 1) line 177을 return 으로 써주든가


근데 생각보다 two pointer 효율이 안좋아서 brute force 기법으로 하는게 나을 수도.. hashmap으로 어떻게 하는지도 보기!
