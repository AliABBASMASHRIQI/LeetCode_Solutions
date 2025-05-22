nums = [1,1,2]
class Solution:
    def thirdMax(self, nums):
        temp_set = set(nums)
        nums = list(temp_set)
        print(nums,"nums")
        if len(nums)<=2:
            print(max(nums))
            return max(nums)
        temp_set = set(nums)
        nums = list(temp_set)
        for i in range(2):
            maximum = max(nums)
            nums.remove(maximum)
            print(maximum)
        print(max(nums),"Answer")
        return max(nums)
            
        
sol = Solution()
sol.thirdMax(nums)