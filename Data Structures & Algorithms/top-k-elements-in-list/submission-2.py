class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for num in nums:
            if d.get(num) == None:
                d[num] = 1
            else:
                d[num] += 1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        l = list(sorted_dict.keys())
        return l[:k]