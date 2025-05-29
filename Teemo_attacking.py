timeSeries = [1,4]
duration = 2
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        temp_set = set()
        for t in timeSeries:
            for i in range(t,t+duration):
                temp_set.add(i)
        print(temp_set)
        return temp_set
        
sol = Solution()
sol.findPoisonedDuration(timeSeries,duration)

## Tle came in my solution so this is optimal 
# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         if not timeSeries:
#             return 0
        
#         total = 0
#         for i in range(len(timeSeries) - 1):
#             # Calculate time until next attack
#             gap = timeSeries[i + 1] - timeSeries[i]
#             # Add either full duration or just the gap (if overlap happens)
#             total += min(duration, gap)
        
#         # Add full duration for the last attack (no attack comes after it)
#         total += duration
        
#         return total

        