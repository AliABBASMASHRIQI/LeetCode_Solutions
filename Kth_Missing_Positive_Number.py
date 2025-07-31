from typing import List
arr = [2,3,4,7,11]
k = 5
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = []
        for num in range(1,arr[len(arr)-1]):
            if num not in arr:
                res.append(num)
        if len(res) <= k:
            for num in range(arr[len(arr)-1]+1,arr[len(arr)-1]+k+1):
                res.append(num)
            
        print(res[k-1])
        return res[k-1]
        
        
# This the optimal solution for two pointers approach has to work again for this problem. Very good solution, had to copy the optimal solution, have to work again on this.

# i = 0
# num = 1 
# while k:
#     if i < len(arr) and arr[i] == num:
#         i += 1
#     else:
#         k -= 1
#         if k == 0:
#             print(num)
#             return num
#     num += 1
                

sol = Solution()
sol.findKthPositive(arr,k)