from typing import Counter, List
licensePlate = "GrC8950"
words = ["measure","other","every","base","accroding","level","meeting","none","marriage","rest"]
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(filter(str.isalpha, licensePlate))
        licensePlate = licensePlate.lower()
        temp_lic = Counter(licensePlate)
        temp = '123456789012345'
        for word in words:       
            if Counter(word) >= temp_lic:
                if len(temp)>len(word):
                    temp = word
        print(temp)
        return temp

# logic was made by me but had to see it again and again for the comaprrision so basically i had to see it have to do thios code again very good question and important too

  
sol = Solution()
sol.shortestCompletingWord(licensePlate,words)      