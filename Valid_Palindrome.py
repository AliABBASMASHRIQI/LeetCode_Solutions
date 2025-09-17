s = "aa"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s)-1
        if len(s) == 0:
            print(True)
            return True
        while i != j and i < j:
            print(s[i],s[j])
            if s[i]!=s[j]:
                print(False)
                return False
            i+=1
            j-=1
        print(True)
        return True
        
 #optimal and easily done in like 10 minutes a very good question just not optimal in space where join should not be used and isalnum should be used in every condition for it to work        

sol = Solution()
sol.isPalindrome(s)