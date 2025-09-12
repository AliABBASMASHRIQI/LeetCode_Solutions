n = 2147483645
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in bin(n)[2:]:
            if int(i) == 1:
                count+=1
        print(count)
        return count
        
#optimal time wise but not space wise adn easy question took m elike 2 minutes and also if we do but n&1  n>>=1 trick space would be optimal 

sol = Solution()
sol.hammingWeight(n)