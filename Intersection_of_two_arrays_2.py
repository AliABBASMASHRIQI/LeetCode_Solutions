nums1 = [1,2,2,1]
nums2 = [2,2]
class Solution:
    def intersect(self, nums1, nums2):
        result = []
        temp_dict = {}
        for num in nums1:
            if num not in temp_dict:
                temp_dict[num] = 1
            else:
                temp_dict[num] +=1
            
        for num in nums2:
            if num in temp_dict:
                result.append(num)
                temp_dict[num]-=1
                if temp_dict[num] == 0:
                    temp_dict.pop(num)
        print(result)
        return result
                

sol = Solution()
sol.intersect(nums1,nums2)