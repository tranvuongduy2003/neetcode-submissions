class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        res = min(heights[0], heights[n - 1]) * (n - 1)

        while l <= r:
            if heights[l] < heights[r]:
                f = heights[l]
                while l + 1 <= n - 1 and heights[l + 1] <= f:
                    l += 1
                l += 1
            else:
                f = heights[r]
                while r - 1 >= 0 and heights[r - 1] <= f:
                    r -= 1
                r -= 1
            res = max(res, min(heights[l], heights[r]) * (r - l))

        return res
            