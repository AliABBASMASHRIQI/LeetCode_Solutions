nums1 = [1,2,2,1]
nums2 = [2,2]
class Solution:
    def intersection(self, nums1, nums2):
        temp_set1 = set(nums1)
        temp_set2 = set(nums2)
        intersection_set = temp_set1 & temp_set2
        result = list(intersection_set)
        return result
        print(result)

sol = Solution()
sol.intersection(nums1,nums2)