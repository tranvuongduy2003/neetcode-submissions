class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (hi + lo) // 2
            s = sum(math.ceil(pile / mid) for pile in piles)
            if s <= h:
                hi = mid
            else: 
                lo = mid + 1
        return hi