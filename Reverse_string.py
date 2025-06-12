s = ["H","a","n","n","a","h"]
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        finish = len(s)-1
        start = 0
        while finish > start:
            s[start],s[finish] = s[finish],s[start]
            start+=1
            finish-=1
        print(s)

sol = Solution()
sol.reverseString(s)
        
        