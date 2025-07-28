from typing import List
arr = [1,2,34,3,4,5,7,23,12]
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = 0
        for num in arr:
            if num%2 !=0:
                flag +=1
                if flag == 3:
                    print(True)
                    return True
            else:
                flag = 0
        print(False)
        return False
    
    
#Did it in 5 minutes very easy no issues     
        
sol = Solution()
sol.threeConsecutiveOdds(arr)