from typing import List
import math
nums = [-1,1,0,-3,3]
temp_arr = []
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        m = math.prod(nums)
        # for index,value in enumerate(nums):
        #     if value == 0:
        #         nums.pop(index)
        #         temp = math.prod(nums)
        #         nums.insert(index,value)
        #         answer.append(temp)
        #         continue
        #     answer.append(m//value)     
        # print(answer)
        # return answer
        n = len(nums)
        
        # Step 1: Create output array and initialize it with 1s
        output = [1] * n
        
        # Step 2: Prefix product
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Step 3: Suffix product (we reuse output array to save space)
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        print(output)
        return output
            

#did the solution but was not Optimal it is a Medium level question and very good also have to do it again as i had to see the optimal solution was successfull in brute force approach.
    
sol = Solution()
sol.productExceptSelf(nums)
        