"""
Given an m x n matrix, return all elements of the matrix in spiral order.

EX 1)
Input: matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

Output: [1,2,3,6,9,8,7,4,5]

"""
class Solution:
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            #add first row/list of matrix
            result += (matrix.pop(0))
            #append last element of all list in order
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            #add reverse of last row/list
            if matrix:
                result += (matrix.pop()[::-1])
            #append first element of all rows/list in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop())
        return  result

