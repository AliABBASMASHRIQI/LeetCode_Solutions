from typing import List
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        row,col = m-1,0
        counter = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                counter+=(n-col)
                row-=1
            else:
                col+=1
        return counter


# i have to see the optimal approach mine was not optimal it has complexity of O(m*n) and optimal approach was O(m+n) have to do again was a really good question                


        
sol = Solution()
sol.countNegatives(grid)
        
'''
        counter = 0
        n = 0
        m = 0
        while len(grid) > 0:
            len_of_block = len(grid[0])
            len_of_list = len(grid)
            if n == len_of_block and m == len_of_list-1:
                print(counter)
                return counter
            if n == len_of_block:
                n = 0
                m+=1            
            if grid[m][n] < 0:
                counter+=1
            n+=1
'''