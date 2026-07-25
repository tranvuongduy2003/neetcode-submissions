class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            l = i + 1
            r = n - 1
            s = 0 - nums[i]
            while l < r:
                while l < n and nums[l] + nums[r] < s: 
                    l += 1
                while r > i and nums[l] + nums[r] > s: 
                    r -= 1
                if l < r and nums[l] + nums[r] == s:
                    res.append([nums[i], nums[l], nums[r]])
                    while r > i + 1 and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                    while l < n - 1 and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
            
            while i < n - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res