#Do it aguian Copied the entire program
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
class Solution:
    def isCovered(self, ranges,left,right) -> bool:
        covered = [False]*51
        for start,end in ranges:
            for i in range(start,end+1):
                covered[i]=True
        for num in range(left,right+1):
            if not covered[num]:
                return False
        return True
            
        
sol = Solution()
sol.isCovered(ranges,left,right)
        