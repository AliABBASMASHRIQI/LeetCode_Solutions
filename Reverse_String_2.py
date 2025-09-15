s = "abcdefg"
k = 2
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # convert to list since strings are immutable
        for i in range(0, len(s), 2 * k):
            # reverse the first k characters in the current 2k block
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
 #copied it had to do again i would have come to a solution but had no time so have to do it again this
            
        
sol = Solution()
sol.reverseStr(s,k)