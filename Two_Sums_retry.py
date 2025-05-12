nums = [2,7,11,15] 
target = 9
class Solution:
    def twoSum(self, nums, target):
        temp_dict = {}
        for index,val in enumerate(nums):
            if target-val not in temp_dict:
                temp_dict[val] = index       
            else:
                temp_arr = []
                temp_arr.append(temp_dict[target-val])
                temp_arr.append(index)
                return temp_arr
        return []
                
        
sol = Solution()
sol.twoSum(nums,target)
        