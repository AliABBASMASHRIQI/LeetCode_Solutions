names = ["Mary","John","Emma"]
heights = [180,165,170]
class Solution:
    def sortPeople(self, names, heights):
        n = len(heights)
        temp_dict = {}
        result = []
        for index in range(n):
            temp_dict[heights[index]] = names[index]
        temp_dict = dict(sorted(temp_dict.items(),reverse=True))
        for values in temp_dict.values():
            result.append(values)
        print(result)
        return result
        
            
    
sol = Solution()
sol.sortPeople(names,heights)
        