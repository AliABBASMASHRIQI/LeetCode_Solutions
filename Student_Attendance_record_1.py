# Did it myself with no issues 
s = "PPALLL"
class Solution:
    def checkRecord(self, s: str) -> bool:
        Absent = 0
        Late = 0
        for attendance in range(len(s)):
            if s[attendance] == 'A':
                Absent +=1 
            if attendance+1 != len(s) and attendance+2 != len(s) and s[attendance] == s[attendance+1] == s[attendance+2]=="L" :
                Late+=3
                print(Late)
                if Late == 3:
                    print(False)
                    return False
            else:
                Late = 0
        if Absent >= 2:
            print(False)
            return False
            
        print(True)
        return True

            
                
            
        
sol = Solution()
sol.checkRecord(s)