class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # index incrementer
        k = 0 
        # check each number
        for num in nums:
            if num != val:
                nums[k] = num
                # increment index (counts valid numbers)
                k+=1
        # returns count of valid numbers
        return k

# Run: O(N) as it loops through an array
# Space: O(1) because only a counter variable is implemented and nums is changed in place

        