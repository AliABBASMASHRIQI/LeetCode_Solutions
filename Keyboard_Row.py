from typing import List
words = ["Hello","Alaska","Dad","Peace"]
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)
        return result
                
#Copied the entire solution logic was not building by me good question have to do again            
    
sol = Solution()
sol.findWords(words)
        