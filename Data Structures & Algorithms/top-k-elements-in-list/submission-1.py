import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = []

        for num,frequency in counts.items():
            heapq.heappush(min_heap, (frequency, num))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        top_k_elements = []
        for frequency, num in min_heap:
            top_k_elements.append(num)

        return top_k_elements 


        