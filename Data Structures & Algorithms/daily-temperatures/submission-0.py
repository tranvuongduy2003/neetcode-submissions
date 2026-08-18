class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i, temp in enumerate(temperatures):
            while bool(stack) and temp > temperatures[stack[-1]]:
                ri = stack.pop()
                res[ri] = i - ri
            stack.append(i)
        return res