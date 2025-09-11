a = "11"
b = "1"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(bin(int(a,2)+int(b,2))[2:])
        return bin(int(a,2)+int(b,2))[2:]
        

sol = Solution()
sol.addBinary(a,b)

# very easy and took like 2 minutes max did it myself only optimal sol
        