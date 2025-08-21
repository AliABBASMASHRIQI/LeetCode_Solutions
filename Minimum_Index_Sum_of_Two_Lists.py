from typing import List
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp_dict = {}
        res_arr = []
        res_val = len(list1)+len(list2)
        for value,word in enumerate(list1):
            temp_dict[word] = value
        print(temp_dict,res_val)
        for value,word in enumerate(list2):
            if word in temp_dict:
                if value+temp_dict[word] < res_val:
                    res_arr.clear()
                    res_arr.append(word)
                    res_val = value+temp_dict[word]
                elif value+temp_dict[word] == res_val:
                    res_arr.append(word)
        print(res_arr)
        return res_arr
                    
# this was the optimal solution adn solved in like 20 minutes good question very easy question did it easily adn this is the most optimal solution                 
            
        
sol = Solution()
sol.findRestaurant(list1,list2)