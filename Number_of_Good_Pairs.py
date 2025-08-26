from typing import List
nums = [1,2,3,1,1,3]
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        temp_dict = {}
        res = 0
        for index,value in enumerate(nums):
            if value in temp_dict:
                temp_dict[value]+=1
            else:
                temp_dict[value] = 1
        for freq in temp_dict.values():
            res+= freq*(freq-1) // 2
        print(res)
        return res
        
      
  # easy question but had to see it didn't knew the formulae for freq have to do agian very god question also this is optimal          
                
            
        
sol = Solution()
sol.numIdenticalPairs(nums)

