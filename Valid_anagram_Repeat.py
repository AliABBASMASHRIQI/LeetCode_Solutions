s="ali"
t="ila"
def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26

        if len(s) != len(t):
            return False

        for index in range(len(s)):
            temp1  = s[index]
            arr[ord(temp1)-ord('a')]+=1
            temp2 =  t[index]
            arr[ord(temp2)-ord('a')]-=1
            
        if all(x == 0 for x in arr ):
            return True
        else:
            return False

isAnagram(s,t)