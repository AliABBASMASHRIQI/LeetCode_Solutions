def nextGreaterElement(nums1, nums2):
   
    temp_dict = {}
    # Monotonic decreasing stack
    stack = []

    
    for num in nums2:
        
        while stack and stack[-1] < num:
            
            temp_dict[stack.pop()] = num
        
        stack.append(num)

    while stack:
        temp_dict[stack.pop()] = -1

    temp_arr = [temp_dict[num] for num in nums1]
    return temp_arr

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]