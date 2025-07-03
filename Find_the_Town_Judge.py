from typing import List
n = 4
trust = [[1,2],[6,4],[3,2],[2,6],[4,5],[6,1],[1,4],[1,5],[2,3],[2,1],[4,3],[4,2],[2,5],[4,1],[2,4],[6,5],[3,5]]
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        banned = []
        temp_dict = {}
        temp_arr = []
        if n == 1:
            return 1
        trust_set = set((a, b) for a, b in trust)
        for person1,person2 in trust:
            if (person2, person1) not in trust_set and  person2 not in banned: #person1 not in banned and
                if person2 not in temp_dict:
                    if person1 not in temp_dict:
                        temp_dict[person2] = [person1]
                    else:
                        temp_dict.pop(person1)
                        banned.append(person1)
                        temp_dict[person2] = [person1]
                        
                else:
                    temp_dict[person2].append(person1)
            else:
                banned.append(person1)
                banned.append(person2)
                if person2 in temp_dict:
                    temp_dict.pop(person2)
                elif person1 in temp_dict:
                    temp_dict.pop(person1)
        print(temp_dict)
        print(banned)
        if not temp_dict:
            print(-1)
            return -1
        else:
            for ans in temp_dict.keys():
                if len(temp_dict[ans]) == n-1:
                    print(ans)
                    return ans
            return -1
            

# min was perfect Logically but the only issue was i had to make set so lookup gets O(1) and also right now it is O(n+t) and space complexity worst case is O(n2) and average is O(n)                     
        
sol = Solution()
sol.findJudge(n,trust)