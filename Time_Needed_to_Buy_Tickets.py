from typing import List
tickets = [2,3,2]
k = 2
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        flag = 0
        index = 0
        sec = 0
        print(tickets[0],"tria;l")
        while flag == 0:
            if k == -1 and tickets[k] != 0:
                k = len(tickets)-1           
            tickets[index] = tickets[index]-1
            sec +=1
            if tickets[k] == 0:
                flag = 1
                print(sec)
                return sec
            numeric = tickets.pop(index)
            k -=1
            if numeric == 0:
                continue
            tickets.insert(len(tickets),numeric)
            
            print(tickets)
            
# correct solution mine was right too but it was coming TLE so this is the correct correct one
'''

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = [(i, t) for i, t in enumerate(tickets)]  # (original_index, tickets_wanted)
        time = 0

        while True:
            person_index, ticket_count = queue.pop(0)  # front of the line
            ticket_count -= 1
            time += 1

            if ticket_count == 0:
                if person_index == k:
                    return time  # your friend is done
            else:
                queue.append((person_index, ticket_count))  # still needs more tickets


Do it again  important 


'''
            
            
        
        
sol = Solution()
sol.timeRequiredToBuy(tickets,k)
        