nums = [3,2,3]
# class Solution:
#     def majorityElement(self, nums):
#         for val in nums:
#             f = nums.count(val)
#             print(f)
#             if f > len(nums)/2:
#                 return val


# Boyer-Moore Voting Algorithm so that Time Limit Exccedded won't come on this --------- 
class Solution:
    def majorityElement(self,nums):
        count = 0
        candidate = None
        for val in nums:
            if count == 0:
                candidate = val
            count+=(1 if val == candidate else -1)
        return candidate
        
sol = Solution()
print(sol.majorityElement(nums))
        