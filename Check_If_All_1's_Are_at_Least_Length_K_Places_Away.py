from typing import List
nums = [0,1, 0,0,1,0,0,1]
k = 2
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag = 0
        first_flag = nums.index(max(nums))
        for index,value in enumerate(nums):
            if index == first_flag:
                flag = k
            if value == 1:
                if flag >= k:
                    flag = 0
                else:
                    print(False)
                    return False
            else:
                flag+=1
        print(True)
        return True

#did it myself with no help easily done         
            
        
sol = Solution()
sol.kLengthApart(nums,k)