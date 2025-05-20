nums = [9,6,4,2,3,5,7,0,1]
class Solution:
    def missingNumber(self, nums):
        # n = len(nums)
        # for num in range(n+1):
        #     if num not in nums:
        #         return num
        
        n = len(nums)
        total = 0
        for num in range(n+1):
            total = total+num
        for num in nums:
            total = total-num
        print(total)
        return total

sol = Solution()
sol.missingNumber(nums)