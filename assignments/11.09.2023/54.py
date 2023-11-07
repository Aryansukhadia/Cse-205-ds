class Solution:
    def spiralOrder(self, matrix):
        answer = []
        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return answer  # Return empty list for empty matrix
        
        m = len(matrix)  # Number of rows
        n = len(matrix[0])  # Number of columns
        row = 0  # Current row index
        col = 0  # Current column index
        count = m * n  # Total number of elements
        
        while m > 0 and n > 0:
            # If only one row left, traverse it
            if m == 1:
                for i in range(col, col + n):
                    answer.append(matrix[row][i])
                break
            
            # If only one column left, traverse it
            if n == 1:
                for i in range(row, row + m):
                    answer.append(matrix[i][col])
                break
            
            # Traverse top row
            for i in range(col, col + n - 1):
                answer.append(matrix[row][i])
            
            # Traverse right column
            for i in range(row, row + m - 1):
                answer.append(matrix[i][col + n - 1])
            
            # Traverse bottom row (if applicable)
            for i in range(col + n - 1, col, -1):
                answer.append(matrix[row + m - 1][i])
            
            # Traverse left column (if applicable)
            for i in range(row + m - 1, row, -1):
                answer.append(matrix[i][col])
            
            row += 1
            col += 1
            n -= 2
            m -= 2
        
        return answer

