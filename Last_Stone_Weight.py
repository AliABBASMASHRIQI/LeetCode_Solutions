stones = [2,7,4,1,8,1]
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)
            if max1 - max2 != 0:
                stones.append(max1 - max2)
        if len(stones) == 0:
            print(0)
            return 0
        print(stones[0])
        return stones[0]

'''
THis is the optinal solution as i do not know how to heapify okayy will have to learn heap later

import heapq

stones = [2, 7, 4, 1, 8, 1]

# Step 1: Convert to negative for max-heap
stones = [-s for s in stones]

# Step 2: Turn list into a heap
heapq.heapify(stones)  # O(n) time

# Step 3: Play the game
while len(stones) > 1:
    stone1 = -heapq.heappop(stones)  # biggest
    stone2 = -heapq.heappop(stones)  # second biggest

    if stone1 != stone2:
        heapq.heappush(stones, -(stone1 - stone2))

# Step 4: Return result
print(-stones[0] if stones else 0)
'''



sol = Solution()
sol.lastStoneWeight(stones)