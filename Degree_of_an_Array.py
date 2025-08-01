from typing import List
from collections import Counter
nums = [1,2,2,3,1,4,2]
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = len(nums)
        first = 0
        last = 0
        temp_dict = {}
        for index,value in enumerate(nums):
            if value in temp_dict:
                temp_dict[value].append(index)
            else:
                temp_dict[value] = [index]
        counts = {key:len(elements) for key,elements in temp_dict.items()}
        max_counts = max(counts.values())
        if max_counts == 1:
            print(nums[0])
            return 1
        high_count_element = [key for key,value in counts.items() if value == max_counts]
        while len(high_count_element) != 0:
            el = high_count_element.pop()
            abc = temp_dict[el]
            first = abc[0]
            last = abc[len(abc)-1]
            length_of_elements = last-first+1
            if length_of_elements < ans:
                ans = length_of_elements
        print(ans)
        
        

# This is the most optimal solution and i dinot even have to copy it from anywhere and it is working perfectly no issues

        
        
sol = Solution()
sol.findShortestSubArray(nums)
        