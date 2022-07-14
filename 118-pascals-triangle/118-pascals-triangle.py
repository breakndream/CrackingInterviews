class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        default_row = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + default_row[-1] + [0]
            new_row = []
            for j in range(len(default_row[-1]) + 1):
                new_row.append(temp[j] +temp[j+1])
            default_row.append(new_row)
        return default_row




         


#1  [0,1,0]
#2  [1,1]  

# 3, [last_list[0],last_list[0]+last_list[1],last_list[1]]
# 4, [last_list[0],last_list[0]+ last_list[1],last_list[1]+ last_list[2],last_list[2]]

# stack? queue? : let's go queue
                