pattern = "aaaa"
s = "dog cat cat dog"

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tem_dict = {}
        temp_dict_pattern = {}
        temp_arr_s = []
        n = 0
        q = 0
        temp_arr_pattern = []
        temp_var = s.split(" ")
        print(temp_var)
        for char in temp_var:
            if char not in tem_dict:
                tem_dict[char] = n
                n+=1
            if char in tem_dict:
                temp_arr_s.append(tem_dict[char])
        print(temp_arr_s)
        print(tem_dict)
        for pat in pattern:
            if pat not in temp_dict_pattern:
                temp_dict_pattern[pat] = q
                q+=1
            if pat in temp_dict_pattern:
                temp_arr_pattern.append(temp_dict_pattern[pat])
        print(temp_arr_pattern)
        print(temp_dict_pattern)
        print(temp_arr_pattern == temp_arr_s)
                
            
            
            

        
sol = Solution()
sol.wordPattern(pattern,s)