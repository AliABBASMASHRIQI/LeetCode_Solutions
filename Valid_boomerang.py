points = [[1,1],[2,3],[3,2]]
class Solution:
    def isBoomerang(self, points):
        res = (points[1][1]-points[0][1])*(points[2][0]-points[0][0]) == (points[2][1]-points[0][1]) * (points[1][0]-points[0][0])
        if res:
            res = False
        else:
            res = True
        print(res)
        return res 
sol = Solution()
sol.isBoomerang(points)