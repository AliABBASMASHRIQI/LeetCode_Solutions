haystack = "hello"
needle = "ll"
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = -1
        temp_dict = {}
        for index,char in enumerate(haystack):
            if char == needle[0]:
                temp_var = haystack[index:len(needle)+index]
                if temp_var == needle:
                    print(index)  
                    return index
        if flag == -1:
            print(flag)
            return -1
                
        
sol = Solution()
sol.strStr(haystack,needle)



#Copied Solution Optimal One 
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # Step 1: Build LPS array
    lps = [0] * len(needle)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Step 2: Match using LPS
    i = j = 0  # i for haystack, j for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == len(needle):
            return i - j  # Match found

        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]  # Use LPS to avoid rechecking
            else:
                i += 1  # Move to next character in haystack

    return -1  # No match
