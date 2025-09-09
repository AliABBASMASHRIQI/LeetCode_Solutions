from typing import List
import math
nums = [2,5,6,9,10]
class Solution:
    def findGCD(self, nums: List[int]) -> int:
            
        print(math.gcd(min(nums),max(nums)))
        return math.gcd(min(nums),max(nums))

sol = Solution()
sol.findGCD(nums)        

#completed very easy all i had to do is use the function do it again but with euclid method
'''
Euclid method
        a = min(nums)
        b = max(nums)
        while b:
            a,b = b,a%b
        return a
'''