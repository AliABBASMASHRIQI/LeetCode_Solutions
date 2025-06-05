flowerbed = [1,0,0,0,0,1]
n = 2
class Solution:
    def canPlaceFlowers(self, flowerbed,n) -> bool:
        # for index,flower in enumerate(flowerbed):
        #     if index == 0 and index+1 == 0 and flower == 0:
        #         flowerbed[index+1] = 1
        #         n -=1
        #     elif (flower == 0 and flowerbed[index-1] != 1) or (flower == 0 and flowerbed[index+1] != 1 ):
        #         if flower == 0 and flowerbed[index-1] != 1:
        #             flowerbed[index-1] = 1
        #             n-=1
        #         else:
        #             flowerbed[index+1] = 1
        #             n-=1
        #     # elif index == len(flowerbed)-1 and index-1 == 0 and flower == 0:
        #     #     flowerbed[index+1] = 1
        #     #     n -=1
        # if n <= 0:
        #     print(True)
        #     print(flowerbed,n)
        #     return True
        #     print(flowerbed)
        # else:
        #     print(False)
        #     print(flowerbed,n)
        #     return False
        # print(flowerbed)
        
    ## had to see The solution i was halfway right only  
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or ( flowerbed[i-1] == 0 )
                empty_right = (i == length-1) or ( flowerbed[i+1] == 0 )
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n-=1
                    if n == 0:
                        return True 
        return n <=0
                
    
                    
                    
                
            
                
    
sol = Solution()
sol.canPlaceFlowers(flowerbed,n)
        