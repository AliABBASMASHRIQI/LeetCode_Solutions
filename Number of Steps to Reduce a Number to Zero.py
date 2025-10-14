class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num %2 == 0:
                num = num//2
                steps+=1
                print(num,steps)
            else:
                num=num-1
                steps+=1
                print(num,steps)
        print(steps)
        return steps
                
# optimal and was very vrey easy took me like 2 minutes and was done in one try with no issues