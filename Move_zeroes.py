nums = [0,1,0,3,12]
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
    zero_counter = 0
    for index,num in enumerate(nums):
        if num == 0:
            zero_counter += 1
    print(zero_counter)
    nums[:] = [num for num in nums if num !=0]
    for i in range(zero_counter):
        nums.append(0)
    print(nums)

sol = Solution()
sol.moveZeroes(nums)

#original Solution done it myself
        # for num in nums:
        #     if num == 0:
        #         nums.remove(0)
        #         nums.append(0)
        # print(nums)
        