from typing import List
accounts = [[1,5],[7,3],[3,5]]
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = 0
        for value in accounts:
            max_num = max(max_num,sum(value))
        print(max_num)
        return max_num
sol = Solution()
sol.maximumWealth(accounts)

# did it in like 2 minutes tops adn very easy question adn is the start of the roadmap will try to not see even one function but again this is optimal solution and i did it by myself