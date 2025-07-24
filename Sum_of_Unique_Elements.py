from typing import List
nums = [1,2,3,2]
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res_arr = [0]*max(nums)
        res_sum = 0
        for index,value in enumerate(nums):
            res_arr[value-1]+=1
        for index,value in enumerate(res_arr):
            if value == 1:
                res_sum+=index+1
        print(res_sum)
        return res_sum
    
#it is an optimal solution regarding the time complexity but space complexity it is not that optimal so issue in that is coming
#space complexity can be reduced in by using collection.counter watch that package once it is easy                
                
            
        

sol = Solution()
sol.sumOfUnique(nums)