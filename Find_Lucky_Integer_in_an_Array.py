from typing import List
arr = [2,2,2,3,3]
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp_dict = {}
        res = -1
        for num in arr:
            if num in temp_dict:
                temp_dict[num]+=1
            else:
                temp_dict[num] = 1
        print(temp_dict)
        for key,value in temp_dict.items():
            if key == value and key > res:
                res = key
        print(res)
        return res
            
sol = Solution()
sol.findLucky(arr)
        