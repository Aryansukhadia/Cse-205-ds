class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        res = []
        while i!=0:
            if i not in arr:
                res.append(i)

            if(len(res) == k) :
                break

            i+=1

        return res[k-1]
        