from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
            rev = int(str(num)[::-1])
            seen.add(rev)
        return len(seen)

# optimal oslution medium question