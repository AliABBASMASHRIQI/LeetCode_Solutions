from sympy import *
s = "05"
class Solution:
    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def sumOfLargestPrimes(self, s) -> int:
        loop_end = 0
        str_cut = 1
        temp_set = set()
        while loop_end <= len(s):
            for i in range(len(s)):
                temp_prime_int = int(s[i:i+str_cut]) 
                if self.is_prime(temp_prime_int):
                    temp_set.add(int(s[i:i+str_cut]))       
            str_cut += 1
            loop_end +=1
        temp_list = [int(temp) for temp in temp_set]
        temp_list.sort()
        print(temp_list,"Listttt")
        if len(temp_list) >= 3:
            result = 0
            result = result+temp_list[len(temp_list)-1]+temp_list[len(temp_list)-2]+temp_list[len(temp_list)-3]
            print(result)
            return result
        else:
            result = 0
            result = sum(temp_list)
            print(result)
            return result
            
            
        

sol = Solution()
sol.sumOfLargestPrimes(s)