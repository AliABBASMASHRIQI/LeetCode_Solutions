class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n & 0xFFFFFFFF, '032b')
        res = n[::-1]
        res = int(res,2)
        print(res)
        return res
# the solution is gettimg completed in constant time but the issue is i have not done any bit manipulation in this 
        