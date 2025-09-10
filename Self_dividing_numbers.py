from typing import List
left = 1
right = 22
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num: int) -> bool:
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True

        result = []
        for n in range(left, right + 1):
            if isSelfDividing(n):
                result.append(n)
        return result
            

# had to copy the entire solution but i understood it adn will have to do it again was an easy question but i had some concept confusion that is why issue occured easy question have to do it again
      
sol = Solution()
sol.selfDividingNumbers()