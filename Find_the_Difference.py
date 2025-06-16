# Did it myself woithout looking at Solutions
s = "abcd"
t = "abcde"
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp_dict = {}
        for value in s:
            if value not in temp_dict:
                temp_dict[value] = 1
            else:
                temp_dict[value]+=1
        print(temp_dict)
        for value in t:
            if value not in temp_dict:
                temp_dict[value] = 1
                print(value)
                return value
            else:
                temp_dict[value] -= 1
                if temp_dict[value] == -1:
                    print(value)
                    return value
        
        
sol = Solution()
sol.findTheDifference(s,t)