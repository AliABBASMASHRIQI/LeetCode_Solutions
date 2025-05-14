nums1 = [4,1,2]
nums2 = [1,3,4,2]

#Copied it again wasn't able to do it have to do again
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        temp_dict = {}
        stack = [] # Monotonic Decreasing Stack
        
        for num in nums2:
            while stack and stack[-1] < num:
                temp_dict[stack.pop()] = num
            stack.append(num)
        
        while stack:
            temp_dict[stack.pop()] = -1
        temp_arr = [temp_dict[num] for num in nums1]
        print(temp_arr)
        return temp_arr

sol = Solution()
sol.nextGreaterElement(nums1,nums2)