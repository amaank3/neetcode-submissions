from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts_words = {}

        for word in strs:
            counts = tuple(sorted(Counter(word).items()))
            if counts in counts_words:
                counts_words[counts].append(word)
            else:
                counts_words[counts] = [word]

        return list(counts_words.values())




        
        