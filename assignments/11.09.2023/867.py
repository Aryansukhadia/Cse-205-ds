class Solution(object):
    def transpose(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, columns = len(A) , len(A[0])

        Newmatrix = [[0]*rows for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                Newmatrix[j][i] = A[i][j]
        return Newmatrix
        
        # return [e for e in zip(*matrix)]\

        
    