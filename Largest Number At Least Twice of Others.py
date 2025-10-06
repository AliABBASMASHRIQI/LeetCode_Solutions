nums = [3,6,1,0]
from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_num = max(nums)
        print(largest_num)
        for val in nums:
            if val > largest_num//2 and val!= largest_num:
                print(-1)
                return -1
        print(nums.index(largest_num))
        return nums.index(largest_num)

sol = Solution()
sol.dominantIndex(nums)


# done easiy no issues and optimal and working all casses