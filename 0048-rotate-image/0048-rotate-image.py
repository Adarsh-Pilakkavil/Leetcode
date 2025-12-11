class Solution(object):
    def rotate(self, matrix):
        for i in range(0,len(matrix),1):
            for j in range(0,i,1):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,len(matrix),1):
            matrix[i]=matrix[i][::-1]
        return matrix