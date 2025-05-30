ops = ["5","-2","4","C","D","9","+","+"]
class Solution:
    def calPoints(self, operations):
        result = []
        for index in range(len(ops)):
            if operations[index] == 'C':
                if result:
                    result.pop()
            elif operations[index] == 'D':
                if result:
                    temp = int(result[len(result)-1]) * 2
                    result.append(temp)
            elif operations[index] == '+':
                if result:
                    temp = int(result[len(result)-1]) + int(result[len(result)-2])
                    result.append(temp)
            elif operations[index].lstrip('+-').isdigit():
                result.append(int(operations[index])) 
        total = sum(result)
        if total:
            print(total)
            return total
        else:
            print(0)
            return 0
            
                
        
        
sol = Solution()
sol.calPoints(ops)