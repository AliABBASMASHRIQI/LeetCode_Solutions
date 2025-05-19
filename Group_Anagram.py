strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:
    def groupAnagrams(self, strs):
        res = []
        temp_dict = {}
        for a in strs:
            temp_var = "".join(sorted(a))
            if temp_var in temp_dict:
                temp_dict[temp_var].append(a) 
            else:
                temp_dict[temp_var] = [a]
        for char in temp_dict.values():
            res.append(char)
            
        print(res)
        return res
        
        
sol = Solution()
sol.groupAnagrams(strs)