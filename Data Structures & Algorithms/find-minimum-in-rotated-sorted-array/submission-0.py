class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        for value in nums[1:]:
            minimum = min(minimum, value)
        return minimum
        