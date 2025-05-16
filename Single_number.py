nums = [4,1,2,1,2]
class Solution:
    def singleNumber(self, nums):
        temp_dict = {}
        for val in nums:
            if val in temp_dict:
                temp_dict[val] = temp_dict[val]+1
            else:
                temp_dict[val] = 1 
        for key,value in temp_dict.items():
            if value == 1:
                return key
    
sol = Solution()
sol.singleNumber(nums)

# Space Complxity O(1) Because a ^ a = 0 and a ^ 0 = a, all pairs cancel out, leaving only the unique number.
class Solution:
    def singleNumber(self, nums):
        ans = 0
        for x in nums:
            ans ^= x
        return ans