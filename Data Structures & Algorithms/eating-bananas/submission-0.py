class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low+high)//2
            total_hours = 0

            for pile in piles:
                hours = (pile+mid -1)//mid
                total_hours+=hours

            if total_hours <= h:
                high = mid
            else:
                low=mid+1

        return low
        
        