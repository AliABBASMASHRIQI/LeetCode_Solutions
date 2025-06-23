from typing import List
heights = [1,1,4,2,1,3]
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        final = 0
        f = list(heights)
        heights.sort()
        for number in range(len(heights)):
            if f[number]!=heights[number]:
                final +=1
        print(final)
        return final
            
        
sol = Solution()
sol.heightChecker(heights)
        
#not the Optimal Solution THis is the Optimal solution

'''
count = [0] * 101  # Index represents height value
for h in heights:
    count[h] += 1
result = 0
current_height = 1  # Start with smallest possible height

for i in range(len(heights)):
    # Find next available height in sorted order
    while count[current_height] == 0:
        current_height += 1
    
    if heights[i] != current_height:
        result += 1
    
    count[current_height] -= 1
'''