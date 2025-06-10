num = 38
class Solution:
    def addDigits(self, num):
        digits = []
        while num >= 10:
            digits.clear()
            while num > 0:
                digit = num % 10
                digits.append(digit)
                num //= 10
            num = sum(digits)
        print(num)
        return num
                
            

sol = Solution()
sol.addDigits(num)

#  Optimal solution by digital root method 
# def addDigits(self, num: int) -> int:
#     if num == 0:
#         return 0
#     return 1 + (num - 1) % 9