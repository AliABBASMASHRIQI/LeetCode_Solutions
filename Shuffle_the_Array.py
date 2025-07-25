from typing import List
nums = [2,5,1,3,4,7]
n = 3
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        flag_x = 0
        flag_y = n
        res = []
        while flag_x < n and flag_y < 2*n: 
            res.extend([nums[flag_x],nums[flag_y]])
            flag_x+=1
            flag_y+=1
            
        print(res)
        return res
#did it myself no help needed very easy did it within 5 min
sol = Solution()
sol.shuffle(nums,n)
        