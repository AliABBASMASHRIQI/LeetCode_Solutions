nums = [6,2,6,5,1,2]
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2]) 

sol = Solution()
sol.arrayPairSum(nums)

# completely copied it and have to do it again no matter what it was very bad 