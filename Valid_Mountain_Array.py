from typing import List
arr = [3,5,5]
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max = 0
        max_pos = 0
        flag = 0
        for index,num in enumerate(arr):
            if num > max:
                max = num
                max_pos = index       
        if max == arr[0] or max == arr[len(arr)-1] or len(arr) < 2:
            print(False)
            return False
        for pos in range(max_pos,len(arr)-1):
            if arr[pos] <= arr[pos+1]:
                flag = 0
                return False
        flag = 1
        print(flag)
        for pos in range(0,max_pos):
            if arr[pos] >= arr[pos+1]:
                flag = 0
                return False
        flag = 1
        print(flag)
        if flag == 1:
            print(True)
            return True
        
#did it myself without help and it took me like half an hour but did it myself with no help and was running in first time only with no issues in any testcase        

sol = Solution()
sol.validMountainArray(arr)
        