class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count_ones = 0
        max_count_ones = 0

        for value in nums:
            if value == 1:
                count_ones +=1
                max_count_ones = max(count_ones, max_count_ones)
            else:
                count_ones = 0

        return max_count_ones






        



