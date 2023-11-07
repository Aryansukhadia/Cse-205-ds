class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result=0
        for i in range(len(nums)):
            if nums[i]==0:
                result=max(result,count)
                count=0
                
            else:
                count+=1
        return max(result,count)