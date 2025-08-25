from typing import List
nums = [1,1,2,2,3,4]
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        temp_dict = {}
        for dup in nums:
            if dup in temp_dict:
                temp_dict[dup]+=1
            else:
                temp_dict[dup] = 1
        for final in nums:
            if temp_dict[final] > 2:
                print(False)
                return False
        print(True)
        return True

# did the solution in like 10 minutes and is working perfectly and is optimal in time and space complexity 
          
sol = Solution()
sol.isPossibleToSplit(nums)