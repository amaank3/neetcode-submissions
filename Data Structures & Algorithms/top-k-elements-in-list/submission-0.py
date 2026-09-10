from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        elements = []
        while k>0:
            max_key = max(num_counts, key=num_counts.get)
            elements.append(max_key)
            num_counts[max_key] = 0
            k-=1
        return elements


        