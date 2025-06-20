columnTitle = "ZY"
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        result = 0
        temp = 0
        for i in range(n-1,-1,-1):
           result +=(ord(columnTitle[temp])-ord('A')+1)* 26**i
           temp+=1
        print(result)
            
            
sol = Solution()
sol.titleToNumber(columnTitle)

#only went as far as just getting barely minimum logic had to see the logic on chat gpt was a math question my logic was multiply 26 * times the first one omes with ord which was completely wrong so have to try it again 