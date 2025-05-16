rowIndex = 3
class Solution:
    def getRow(self, rowIndex):
        res = [[1]]
        for index in range(rowIndex+1):
            temp = [0] + res[index] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        print(res[rowIndex])
                

sol = Solution()
sol.getRow(rowIndex)