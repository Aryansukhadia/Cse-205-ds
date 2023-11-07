class Solution:
    def findNumbers(self, nums):
        x=[]
        for y in nums:
            x.append(len(str(y)))
        c=0
        for y in x:
            if(y%2==0):
                c+=1
        return c  