class Solution:
    def search(self, nums: List[int], target: int):

        left = 0
        right = len(nums) - 1

        while left <= right:  

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # LEFT HALF IS SORTED
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT HALF IS SORTED
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1 
