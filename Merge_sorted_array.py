nums1 = [1,2,6,0,0,0]
nums2 = [2,3,5]
m = 3
n = 3   
class Solution:
    def merge(self, nums1,nums2,m,n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for value in nums1[m::]:
            print(nums1.pop())
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

sol = Solution()
sol.merge(nums1,nums2,m,n)



#Copied Optimal Solution 

class Solution:
    def merge(self, nums1, nums2, m, n):
        # Start from the end
        i = m - 1  # Last element in the actual nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1 (including 0s)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements left in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


sol = Solution()
sol.merge(nums1,nums2,m,n)