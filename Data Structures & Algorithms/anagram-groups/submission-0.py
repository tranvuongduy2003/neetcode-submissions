class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if d.get(sorted_s) == None:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return list(d.values())