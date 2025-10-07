from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        words = s1.split()
        words.extend(s2.split())
        word_count = Counter(words)
        print(words)
        print(word_count)
        unique_elements = [item for item,freq in word_count.items() if freq ==1]
        print(unique_elements)
        return unique_elements
    
    
# this is optimal and is working fine perfectly


        