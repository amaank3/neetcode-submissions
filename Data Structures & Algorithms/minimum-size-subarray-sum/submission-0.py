class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                min_length = min(min_length, right - left + 1)
                total_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length


        