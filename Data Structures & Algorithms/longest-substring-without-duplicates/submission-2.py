class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        l, r, res = 0, 1, 1
        d = {}
        d[s[l]] = 0

        while l < r and r < n:
            if d.get(s[r]) != None and d.get(s[r]) >= l:
                res = max(res, r - l)
                l = d[s[r]] + 1
            d[s[r]] = r
            r += 1
        res = max(res, r - l)
        return res
    

