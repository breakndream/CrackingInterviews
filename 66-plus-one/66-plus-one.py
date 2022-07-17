class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_number = 0
        count = len(digits) - 1
        
        for i in digits:
            new_number += i * 10 ** count
            count -= 1
        
        new_number += 1
        
        new_array = []
        for i in str(new_number):
            new_array.append(int(i))
            
        return new_array
            
        

            
        