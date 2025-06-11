n = 15
class Solution:
    def fizzBuzz(self, n):
        answer = []
        for number in range(1,n+1):
            if number%3 == 0 and number%5 == 0:
                answer.append("FizzBuzz")
            elif number%3 == 0:
                answer.append("Fizz")
            elif number%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(number))
        print(answer)
        return answer
                

sol = Solution()
sol.fizzBuzz(n)
        