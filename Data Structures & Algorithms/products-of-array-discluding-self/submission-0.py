from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = nums.copy()
        for i in range(0, n):
            product = 1
            for j in range(0, n):
                if i != j:
                    product *= nums[j]
            r[i] = product
        return r