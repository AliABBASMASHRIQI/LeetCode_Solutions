nums = [4,3,2,7,8,2,3,1]
class Solution:
    def findDisappearedNumbers(self, nums):
        temp_dict = {}
        result = []
        for index in range(1,len(nums)+1):
            temp_dict[index] = 0
        for num in nums:
            if num in temp_dict:
                temp_dict[num] = temp_dict[num]+1
        for keys,values in temp_dict.items():
            if values == 0:
                result.append(keys)
        print(result)
        return result

sol = Solution()
sol.findDisappearedNumbers(nums)
        