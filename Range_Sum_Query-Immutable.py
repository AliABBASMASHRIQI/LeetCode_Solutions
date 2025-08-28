from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for num in range(left,right+1):
            res+= self.nums[num]
        print(res)
        return res
            
# Easy Question also optimal but one improvement can be done is create a prefix sum in init so each query takes O(1) only             
        
obj = NumArray([-2, 0, 3, -5, 2, -1])
obj.sumRange(0,2)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)