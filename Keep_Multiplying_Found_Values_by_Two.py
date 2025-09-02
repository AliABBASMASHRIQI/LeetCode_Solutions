from typing import List
nums = [5,3,6,1,12]
original = 3
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original*=2
        print(original)
        return original
sol = Solution()
sol.findFinalValue(nums,original)

# very easy question was done by me in like 2 minutes have to try harder from now on very easy question 