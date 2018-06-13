class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = []
        if len(matrix) == 0:
            return l
        rowBegin = 0
        rowEnd = len(matrix)-1
        colBegin = 0
        colEnd = len(matrix[0])-1
        
        total = len(matrix)*len(matrix[0])
        
        while (rowBegin<=rowEnd) and (colBegin <= colEnd):
            #traversing right
            for i in range(colBegin, colEnd+1):
                l.append(matrix[rowBegin][i])   
            if len(l) == total:
                return l
            rowBegin += 1
           
            #traversing down
            for i in range(rowBegin, rowEnd+1):
                l.append(matrix[i][colEnd])
            if len(l) == total:
                return l
            colEnd -= 1
            
            #traversing left
            for i in range(colEnd,colBegin-1,-1):
                l.append(matrix[rowEnd][i])
            if len(l) == total:
                return l
            rowEnd -= 1
            
            #traversing up
            for i in range(rowEnd, rowBegin-1, -1):
                l.append(matrix[i][colBegin])
            if len(l) == total:
                return l
            colBegin += 1
            
            
        return l       
    