class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        max_length = 0

        for num in nums:
            d[num] = False

        for key in list(d.keys()):
            if d[key] == True:
                continue
            d[key] = True
            ml = 1
            next_key = key + 1
            while d.get(next_key) != None:
                d[next_key] = True
                ml += 1
                next_key += + 1
            prev_key = key - 1
            while d.get(prev_key) != None:
                d[prev_key] = True
                ml += 1
                prev_key -= 1
            max_length = max(ml, max_length)

        return max_length
            
            
