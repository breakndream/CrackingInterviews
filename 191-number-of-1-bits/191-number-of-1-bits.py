class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n,'b')
        counter = 0 
        for i in str(n):
            
            if i == '1':
                counter += 1
            else:
                continue

        return counter

