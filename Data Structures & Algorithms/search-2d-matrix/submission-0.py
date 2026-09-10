class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for parts in matrix:
            if self.binarySearch(parts,target):
                return True
                break
        return False


    def binarySearch(self,nums, target):
        left = 0
        right = len(nums)-1

        while left <=right:
            middle = (left+right)//2

            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle-1
            else:
                return True
                break
        return False
        