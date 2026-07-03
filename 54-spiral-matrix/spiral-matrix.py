class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])

        rowStart = 0
        colStart = 0
        rowEnd = n-1
        colEnd = m-1

        c = 0
        ans = []
        total = n*m

        while c < total:
            #for printing TOP_ROW
            for i in range(colStart, colEnd + 1):
                ans.append(matrix[rowStart][i])
                c += 1
            rowStart += 1

            if c == total:
                break
            
            #for printing END_COLUMN
            for i in range(rowStart, rowEnd + 1):
                ans.append(matrix[i][colEnd])
                c += 1
            colEnd -= 1

            if c == total:
                break
            
            #for printing ROW_END
            for i in range(colEnd, colStart - 1, -1):
                ans.append(matrix[rowEnd][i])
                c += 1
            rowEnd -= 1

            
            if c == total:
                break
            
            #for printing ROW_START
            for i in range(rowEnd, rowStart - 1, -1):
                ans.append(matrix[i][colStart])
                c += 1
            colStart += 1
    
        return ans