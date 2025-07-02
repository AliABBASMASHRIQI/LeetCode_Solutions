import re
from typing import List
import string
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        temp_dict = {}
        temp_arr = []
        count = 0
        paragraph = paragraph.lower()
        temp_arr = re.split(r'[^\w]+', paragraph)
        temp_arr = [word for word in temp_arr if word]
        print(temp_arr)
        for word in temp_arr:
            if word not in temp_dict:
                temp_dict[word]=1
            else:
                temp_dict[word]+=1
        for keys, value in list(temp_dict.items()):
            if value > count:
                if keys in banned:
                    temp_dict.pop(keys)
                    continue  
                count = value
                temp_var = keys
        print(temp_var)
        return temp_var

            
                
        
sol = Solution()
sol.mostCommonWord(paragraph,banned)