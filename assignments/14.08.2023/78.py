class Solution:
    def subsets(self, nums):
        n = len(nums)
        if n == 0:
            return [[]]
        nums.sort()
        res1 = self.subsets(nums[:n-1])
        res2 = self.subsets(nums[:n-1])
        for sub in res1:
            sub.append(nums[-1])
        res1.extend(res2)
        return res1
