import math
digits = [1,2,3]
class Solution:
    def plusOne(self, digits):
        power = 1
        f = 0
        for val in digits[::-1]:
            f = f + val * power
            power = power*10
        f=f+1
        temp_arr = [int(d) for d in str(f)]
        return temp_arr


sol = Solution()
sol.plusOne(digits)
        