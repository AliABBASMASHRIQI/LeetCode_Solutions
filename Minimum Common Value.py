from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        temp_set1 = set(nums1)
        temp_set2 = set(nums2)
        common = temp_set1 & temp_set2
        if not common:
            return -1  
        return min(common)
# optimal and it is working fine and done by me alone