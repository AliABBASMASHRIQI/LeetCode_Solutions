from typing import List
from collections import Counter
arr = [1,2]
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp_dict = Counter(arr)
        temp_arr = []
        for values in temp_dict.values():
            temp_arr.append(values) 
        temp_set = set(temp_arr)
        if len(temp_arr) == len(temp_set):
            print(True)
            return True
        print(False)
        return False
 
 
#did it myself with no help whatso ever did it easily within 10 minutes this is a has problem too       
sol = Solution()
sol.uniqueOccurrences(arr)