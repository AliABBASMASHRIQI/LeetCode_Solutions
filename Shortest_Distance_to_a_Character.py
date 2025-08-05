from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        prev = float('-inf')
        
        # Left to right pass
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev if prev != float('-inf') else float('inf')
        
        # Right to left pass
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i if prev != float('inf') else float('inf'))
        
        return result
#copied the entire solution didnot even tried to solve it was getting out of my league tbh but understood the solution 