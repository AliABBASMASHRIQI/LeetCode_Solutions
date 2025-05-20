nums = [1,2,3,1,2,3]
k = 2
class Solution:
    def containsNearbyDuplicate(self, nums,k):
        temp_dict = {}
        for index,value in enumerate(nums):
            if value in temp_dict and index - temp_dict[value] <=k:
                print(True)
                return True
            temp_dict[value] = index
        print(False)
        return False
          
        
    
sol = Solution()
sol.containsNearbyDuplicate(nums,k)