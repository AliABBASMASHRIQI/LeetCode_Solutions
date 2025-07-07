from typing import List
arr = [37,12,28,9,100,56,80,5,12]
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_map = {num:rank+1 for rank,num in enumerate(sorted_unique)}
        return [rank_map[num] for num in arr]
             
                
  #solution was understood perfectly but copied everything and i was very off with the Solution of myself      
        
sol = Solution()
sol.arrayRankTransform(arr)
        