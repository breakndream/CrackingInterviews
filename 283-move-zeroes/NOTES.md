### 1st Try:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for i in nums:
            if i == 0 :
                nums.remove(0)
                counter += 1
        while counter:
            nums.append(0)
            counter -=1
        return nums
        
 근데 저렇게하면 **remove()가 해당 되는 게 여러 개 있으면 single element 만 지워버림..**  
 그래서 [0,0,1] 이 input인 경우에는 for loop이 제대로 돌아가지 않고 나가버리더라.. 왜 그런지는 모르겠움 </br>
그래서 for loop 말고 while loop 으로 만들어서 counter increment 해줬다!!
