g = [1,2]
s = [1,2,3]
class Solution:
    def findContentChildren(self, g,s):
        g.sort()
        s.sort()
        flag = 0
        for char in s:
            if char in g:
                g.remove(char)
                #s.remove(char)
                flag+=1
        print(flag)
        return flag

sol = Solution()
sol.findContentChildren(g,s)

##optimised and working Solution
# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()  # sort greed factors
#         s.sort()  # sort cookie sizes
#         child = 0
#         cookie = 0
        
#         # while we have both children and cookies to consider
#         while child < len(g) and cookie < len(s):
#             if s[cookie] >= g[child]:  # cookie satisfies the child
#                 child += 1  # move to next child
#             cookie += 1  # move to next cookie (either way)
        
#         return child
        