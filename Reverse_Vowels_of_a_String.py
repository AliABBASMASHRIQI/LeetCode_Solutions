s = "leetcode"
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0 
        j = len(s)-1
        vowel_list = ['a','e','i','o','u']
        temp = list(s)  
        while i < j:
            if temp[i].lower() in vowel_list and temp[j].lower() in vowel_list:
                temp[i],temp[j] = temp[j],temp[i] 
                i+=1
                j-=1
            elif temp[i].lower() in vowel_list and temp[j].lower() not in vowel_list:
                j-=1
            elif temp[j].lower() in vowel_list and temp[i].lower() not in vowel_list:
                i+=1
            elif temp[i].lower() not in vowel_list and temp[j].lower() not in vowel_list:
                i+=1
                j-=1
        temp = ''.join(temp)
        print(temp)
        return temp
            
# The solution is optimal and works just fine did while in the meeting      
        
sol = Solution()
sol.reverseVowels(s)