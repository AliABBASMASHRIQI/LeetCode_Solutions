def removeElement(nums,val):
    temp_arr = []
    for num in nums:
        if num != val:
            temp_arr.append(num)
    k = len(temp_arr)
    nums.clear()
    nums.extend(temp_arr)
    print(k,temp_arr)   
    return k

removeElement([0,1,2,2,3,0,4,2],2)



'''
OPtimal Solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the position for next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the current valid element at position k
                k += 1  # Increment k for the next valid position
        return k  # Return the new length of the modified array

'''