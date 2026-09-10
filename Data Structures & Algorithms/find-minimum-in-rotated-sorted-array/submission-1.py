class Solution:
    def findMin(self, nums: List[int]) -> int:

        #O(n) approach
        # minimum = nums[0]
        # for value in nums[1:]:
        #     minimum = min(minimum, value)
        # return minimum

        # O(logn) approach
        
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
        