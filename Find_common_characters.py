from typing import Counter
 #Had to copy Completely 

words = ["bella","label","roller"]
class Solution:
    def commonChars(self, words):
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        result = []
        for char,freq in common.items():
            result.extend([char]*freq)
        return result
                
        
    
sol = Solution()
sol.commonChars(words)
        