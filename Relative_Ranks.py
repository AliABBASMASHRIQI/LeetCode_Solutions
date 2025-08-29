from typing import List
score = [10,3,8,9,4]
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp_dict = {}
        temp_arr = score.copy()
        temp_arr.sort(reverse=True)
        for num in range(len(temp_arr)):
            if num+1 == 1:
                temp_dict[temp_arr[num]] = "Gold Medal"
            elif num+1 == 2:
                temp_dict[temp_arr[num]] = "Silver Medal"
            elif num+1 == 3:
                temp_dict[temp_arr[num]] = "Bronze Medal"
            else:        
                temp_dict[temp_arr[num]] = num+1
        print(temp_dict)
        temp_arr.clear()
        for val in score:
            temp_arr.append(str(temp_dict[val]))
        print(temp_arr)
        return temp_arr
    
# optimal solution no issues in that adn was easy adn took me like 10-15 minutes but was easy  
sol = Solution()
sol.findRelativeRanks(score)
        