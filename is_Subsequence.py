s = "abc"
t = "ahbgdc"
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == len(s)
                
            
 #Copied the Entire Solution but could have solved if enough time was given to me by myself            
        
sol = Solution()
sol.isSubsequence(s,t)