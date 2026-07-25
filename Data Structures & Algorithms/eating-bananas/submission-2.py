class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        box = piles
        upperLimit = max(box)
        lowerLimit = 1
        ans = upperLimit
        while lowerLimit <= upperLimit:
            mid = lowerLimit + (upperLimit - lowerLimit) // 2
            hrs = 0
            for b in box:
                hrs += math.ceil(b/mid)
            
            if hrs <= h:
                ans = mid
                upperLimit = mid - 1
            
            else:
                lowerLimit = mid + 1
        
        return ans
        