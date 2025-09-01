from typing import List
arr = [0,-2,2]
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp_dict = {}
        for index,value in enumerate(arr):
            if value*2 in temp_dict:
                print(temp_dict[value*2],index)
                return True
            else:
                temp_dict[value] = index
                
                
        for index,value in enumerate(arr):
            if value*2 in temp_dict and temp_dict[value*2]!= index:
                print(temp_dict[value*2],index)
                return True     
        print(temp_dict)
        return False

# This is Optimal code adn works perfectly adn took me like 10 minutes adn was done by myself only Easy Question no issues

sol = Solution()
sol.checkIfExist(arr)
        