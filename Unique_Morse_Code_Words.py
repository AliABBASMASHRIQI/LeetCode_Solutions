from typing import List
morse_arr =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin","zen","gig","msg"]
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        temp_set = set()
        # arr_num = 0
        # for num_char in range(97,123):
        #     temp_dict[chr(num_char)] = morse_arr[arr_num]
        #     arr_num+=1
        # print(temp_dict)
        # temp = ord('g')
        # print(morse_arr[temp-ord('a')])
        for word in words:
            temp_list = []
            for alpha in word:
                temp_list.append(morse_arr[ord(alpha) - ord('a')])
            temp = ''.join(temp_list)
            temp_set.add(temp)
            
        print(temp_set)
        return len(temp_set)

#did it with my own no help needed only minor issue was done by using append and list that's it not a major thing loigc was my own code my own no issues      
sol = Solution()
sol.uniqueMorseRepresentations(words)  