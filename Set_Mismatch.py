from typing import List

nums = [1,1]
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp_dict = {}
        res_arr = []
        for num in nums:
            if num in temp_dict:
                temp_dict[num] +=1
            else:
                temp_dict[num] = 1
        print(temp_dict)
        for key,value in temp_dict.items():
            if value > 1:
                res_arr.append(key)
        print(res_arr,"Trial")
        for num in range(1,len(nums)+1):
            if num not in temp_dict:
                res_arr.append(num)
                print(res_arr)
                return res_arr
            
#Completed The Question was Pretty easy to do obviously had some wrong submissions and did then easily
#Time Complexity is O(n) and Space Complexity is O(n) too but can be reduced to O(1) using cyclic sort or math tric
sol = Solution()
sol.findErrorNums(nums)