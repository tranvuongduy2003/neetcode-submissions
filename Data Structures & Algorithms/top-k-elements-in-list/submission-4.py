class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        freq = [[] for i in range(0, n + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        print(list(count.items()))
        
        for c in list(count.items()):
            freq[c[1]].append(c[0])
        
        r = []
        for i in range(n, 0, -1):
            if (k <= 0):
                break
            fl = len(freq[i])
            if fl > 0:
                r.extend(freq[i][:k])
            k -= fl

        return r    