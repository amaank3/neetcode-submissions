class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  
        for i in range(len(nums)):
            current_num = nums[i]
            needed = target - current_num
            if needed in seen:
                return [seen[needed], i]  
            seen[current_num] = i  
        