nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums):
        # import pdb
        # pdb.set_trace()
        # i = 0
        # j= i+1
        # k = j+1
        # temp_arr = []
        # while j != len(nums)-1 :
        #     if nums[i]+nums[j]+nums[k] == 0:
        #         temp_arr.append([nums[i],nums[j],nums[k]])
        #         k = k+1
        #     else:
        #         k = k+1      
        #     if k == len(nums)-1:
        #         i = i+1 
        #         j = i+1
        #         k = j+1
        #     if k == len(nums)-1 and j == len(nums)-2:
        #         exit()
        # print(temp_arr)
        # return temp_arr
        # n = len(nums)
        # temp_arr = []

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in temp_arr:
        #                     temp_arr.append(triplet)
        # print(temp_arr)
        # return temp_arr
        nums.sort()
        n = len(nums)
        result = []
        for i in range (n-2):
            if i > 0 and nums [i]==nums[i-1]:
                continue
            left,right = i+1,n-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left<right and nums[left] == nums[left - 1]:
                        left +=1
                    while left<right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -=1
                    
                    
        print(result)
        return result
                    
                
  


sol = Solution()
sol.threeSum(nums)        