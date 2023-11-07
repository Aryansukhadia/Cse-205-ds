class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        Max = 0
        for i in accounts:
            Sum = 0
            for k in i:
                Sum = Sum + k
            if Max<Sum:
                Max = Sum
        return Max
        # return max([sum(acc) for acc in accounts])
        