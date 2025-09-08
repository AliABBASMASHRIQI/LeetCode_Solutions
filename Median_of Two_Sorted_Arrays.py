from typing import List
nums1 = [1,2]
nums2 = [3,4]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0

        merged = []
        while i <len(nums1) and j <len(nums2):
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j+=1
            else:
                merged.append(nums1[i])
                i+=1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        print(merged)
        n = len(merged)
        if n%2 == 0:
            print("even")
            print(n//2)
            print(merged[n//2])
            print((merged[n//2]+merged[(n//2)-1])/2)
            return (merged[n//2]+merged[(n//2)-1])/2
        else:
            print("odd")
            print(merged[(n)//2])
            return merged[(n)//2]
            
          
# this works but this is not optimal solution i did not see the optimal solution because i want to try it myself but i will come back to this next week haev to do it again the solution works but not optimal                
        

sol = Solution()
sol.findMedianSortedArrays(nums1,nums2)        