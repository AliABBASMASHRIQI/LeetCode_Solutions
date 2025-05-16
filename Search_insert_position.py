nums = [1,3,5,6,9]
target = 7
class Solution:
    def searchInsert(self, nums, target):
        # import pdb
        # pdb.set_trace()
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return low

sol = Solution()
f = sol.searchInsert(nums,target)
print(f)