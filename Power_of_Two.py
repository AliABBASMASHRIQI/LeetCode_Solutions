
n = 16
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        
        
sol = Solution()
sol.isPowerOfTwo(n)

#Copied the entire thing but was a good question really should do it again this one