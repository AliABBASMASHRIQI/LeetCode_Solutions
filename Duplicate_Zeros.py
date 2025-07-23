from typing import List
arr = [0,4,1,0,0,8,0,0,3]
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i=0
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
                continue
            i+=1
        print(arr)
        return arr  

'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = 0
        
        # Count zeros that can be duplicated within array length
        for i in range(n):
            if arr[i] == 0:
                zeros += 1
        
        # i points to last element in original array
        i = n - 1
        # j points to last position in "expanded" array
        j = n + zeros - 1
        
        # Process backward
        while i < j:
            # If j is within bounds, copy arr[i] to arr[j]
            if j < n:
                arr[j] = arr[i]
            
            # If element is zero, duplicate it
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            
            i -= 1
            j -= 1

'''                

#did the solution but wasn't ab;e to do the optimised solutions having issue in that have to revoisit two pointers again easy question still had to llok for optimised solution            

sol = Solution()
sol.duplicateZeros(arr)
        