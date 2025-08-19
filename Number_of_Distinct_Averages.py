from typing import List
nums = [4,1,4,0,3,5]
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        min_flag = 0
        max_flag = len(nums)-1
        temp_set = set()
        while min_flag < max_flag:
            temp_set.add((nums[min_flag]+nums[max_flag])/2)
            min_flag+=1
            max_flag-=1
        print(len(temp_set))
        return len(temp_set)
    
# this is done completely by me and very easy did it in like actually 5 minutes max with no error
sol = Solution()
sol.distinctAverages(nums)