class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bk = [0] * 1000
        a = []
        for num in nums:
            if bk[num] == 0:
                a.append(num)
            bk[num] += 1
        r = sorted(a, key=lambda num : bk[num], reverse=True)
        return r[0:k]
        
        
