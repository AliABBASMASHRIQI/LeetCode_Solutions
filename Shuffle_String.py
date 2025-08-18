from typing import List
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp_dict = {}
        words = []
        n = len(indices)-1
        while n >=0:
            temp_dict[indices[n]] = s[n]
            n-=1
        print(temp_dict)
        for f in range(len(indices)):
            words.append(temp_dict[f])
        print(''.join(words))
        return ''.join(words)
            
            
# this is the optimal solution and very easy done in like 10 minutes     

sol = Solution()
sol.restoreString(s,indices)     