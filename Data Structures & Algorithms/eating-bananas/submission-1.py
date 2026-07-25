class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        n = len(piles)
        ans = j
        while i<=j:

            mid = i + (j-i)//2
            hrs = 0

            for p in piles:
                hrs += math.ceil(p/mid)
            
            if hrs<=h:
                ans = mid
                j = mid-1

            else:
                 i = mid+1
        return ans
