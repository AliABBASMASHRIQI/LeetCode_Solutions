from typing import List
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        temp_set = set()
        nums1 = set(nums1)
        nums2 =set(nums2)
        nums3 = set(nums3)
        temp_set.update(nums1.intersection(nums2))
        temp_set.update(nums2.intersection(nums3))
        temp_set.update(nums1.intersection(nums3))
        
        print(temp_set)
        
        
        print(list(temp_set))
        return list(temp_set)
    
# did it myself not very hard adn easy solution had to see how to do syntax for intersection but overall easy 
sol = Solution()
sol.twoOutOfThree(nums1,nums2,nums3)
        