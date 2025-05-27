nums = [-2147483648,0,2,3,4,6,8,9]
class Solution:
    def summaryRanges(self, nums):
        start = 0
        result = []
        if len(nums) == 0:
            return result
        for i in range(1,len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1]+1:
                if start == i-1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i-1]}")
        return result
           

sol = Solution()
sol.summaryRanges(nums)


 #original solution
        #  counter = 0
        # temp_arr = []    
        # result = []
        # if len(nums) == 0:
        #     return result
        # for i in range(nums[0],nums[len(nums)-1]+1):
#  if i == nums[counter] :
#                 temp_arr.append(nums[counter])
#                 counter += 1
#             else:

#                 if len(temp_arr) == 0:
#                     continue
#                 if len(temp_arr) == 1:
#                     str = f"{temp_arr[0]}"
#                     result.append(str)
#                     temp_arr.clear()

#                 else:    
#                     str = f"{temp_arr[0]}->{temp_arr[len(temp_arr)-1]}"
#                     result.append(str)
#                     temp_arr.clear()
 
#             if counter == len(nums):
#                 if len(temp_arr) == 1:
#                     str = f"{temp_arr[0]}"
#                     result.append(str)
#                     temp_arr.clear()
#                 else:    
#                     str = f"{temp_arr[0]}->{temp_arr[len(temp_arr)-1]}"
#                     result.append(str)
#                     temp_arr.clear()
                              
#         print(result)
#         return result