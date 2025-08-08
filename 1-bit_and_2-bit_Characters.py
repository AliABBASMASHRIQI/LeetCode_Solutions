from typing import List
bits = [0,1,0]
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag1 = 0
        flag2 = 1

        while flag1 < len(bits) or flag2 < len(bits):
            if flag1 == len(bits)-1 and bits[flag1] == 0:
                print(True)
                return True
            elif bits[flag1] == 1 and bits[flag2] == 0:
                flag1+=2
                flag2+=2
            elif bits[flag1] == 0 and bits[flag2] == 0:
                
                flag1+=1
                flag2+=1
            elif bits[flag1] == 1 and bits[flag2] == 1:
                
                flag1+=2
                flag2+=2
            elif bits[flag1] == 0 and bits[flag2] == 1:
                flag1+=1
                flag2+=1

        print(False)
        return False

# did it comletely by myself with no help took me around 20 minutes      
        
        
sol = Solution()
sol.isOneBitCharacter(bits)
        