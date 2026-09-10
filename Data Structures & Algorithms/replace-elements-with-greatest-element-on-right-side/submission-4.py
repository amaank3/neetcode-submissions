class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # initial max = -1
        # traverse in reverse
        # update max as we go backwards

        right_max = -1

        # Traverse each element in reverse
        for i in range(len(arr)-1, -1, -1):
            # Update new max with current max and current value
            new_max = max(right_max, arr[i])
            # Replace current value with right max value
            arr[i] = right_max
            # Replace right max value with the new max 
            right_max = new_max

        # Return array
        return arr


Time: O(N)
Space: O(1)