class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row*col - 1
        while l<=r:
            mid = (l+r) // 2
            mr = mid // col
            mc = mid % col
            if matrix[mr][mc] == target:
                return True
            if matrix[mr][mc] > target:
                r = mid - 1
            if matrix[mr][mc] < target: 
                l = mid + 1
        return False           