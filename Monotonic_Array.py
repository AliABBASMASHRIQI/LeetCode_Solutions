from typing import List
nums = [1,1,0]
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = "a"
        # temp1 = list(nums)
        # temp2 = list(nums)
        # temp1.sort(reverse=True)
        # temp2.sort()
        # #print(temp1,temp2)
        # if nums == temp1 or nums == temp2:
        #     print(True)
        #     return True
        # return False
        '''
        Did it myself the upside one which was pretty easy no issue wasnt able to optimize tho
        The below one was my version of failed code optimization
        '''
        # flag = "a"
        # if nums[0] > nums[1]:
        #     flag = "D"
        # else:
        #     flag = "I" 
            
        # if flag == "I":
        #     for num in range(len(nums)):
        #         if num == len(nums)-1 or nums[num] <= nums[num+1]:
        #             pass
        #         else:
        #             return False
        #     return True
        
        # if flag == "D":
        #     for num in range(len(nums)):
        #         if num == len(nums)-1 or nums[num] >= nums[num+1]:
        #             pass
        #         else:
        #             return False
        #     return True
        
        #-----------------------------------------------------------------------
#this is the optimized code Copied it entirely and the just above one is my trial to  optimize the code
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False
        
        return increasing or decreasing
     

sol = Solution()
print(sol.isMonotonic(nums))
        