def twoSum(nums, target):
    temp_dict = {}
    i = 0
    for num in nums:
        temp = target-num
        if num in temp_dict:
            temp_value = temp_dict[num]
            return temp_value,i
        temp_dict[temp] = i
        i=i+1
nums = [3,4,5,6]
# import pdb
# pdb.set_trace()     
x = twoSum(nums,7)
print(x)