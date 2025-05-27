nums = [1,1,0,1,1,1]

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # flag = 0
        # temp = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         flag += 1
        #     elif nums[i]!=1:
        #         if flag > temp:
        #             temp = flag
        #             flag = 0
        #     if i == len(nums)-1:
        #         if flag > temp:
        #             temp = flag
        # print(temp)
        # return temp
        
        flag = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                flag += 1
            else:
                temp = max(temp, flag)
                flag = 0
        # Final update after loop in case last elements were 1s
        temp = max(temp, flag)
        return temp
                
        
                
            
    
sol = Solution()
sol.findMaxConsecutiveOnes(nums)