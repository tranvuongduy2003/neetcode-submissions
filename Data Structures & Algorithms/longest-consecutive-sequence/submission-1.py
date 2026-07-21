class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        ml = 0
        for num in nums:
            d[num] = 1
        for key in list(d.keys()):
            if d[key] != 1:
                continue
            cur = d[key]
            i = key + 1
            while d.get(i) != None:
                d[i] = cur + 1
                cur = d[i]
                i += 1
            ml = max(ml, cur)
        return ml
            
            
