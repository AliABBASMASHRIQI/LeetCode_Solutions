from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp_set1 = set(nums1)
        temp_set2 = set(nums2)
        print(temp_set1)
        print(temp_set2)
        sum_res1 = temp_set1-temp_set2
        sum_res2 = temp_set2-temp_set1
        sum_res1 = list(sum_res1)
        sum_res2 = list(sum_res2)
        print(sum_res1)
        print
        result = []
        print(result)
        result.append(sum_res1)
        result.append(sum_res2)
        print(result)
        return result
        
# optimal solution and was done in one go optimal and easy was done by me