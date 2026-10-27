class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(l):    
            start = 0
            end = len(l)-1
            while start <= end:
                mid = ((end + start)//2)
                if target > l[mid]:
                    start = mid+1
                elif target < l[mid]:
                    end = mid-1
                else:
                    return True
            return False
        start = 0
        end = len(matrix)-1
        while start <= end:
            mid = ((end + start)//2)
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                return binarySearch(matrix[mid])
            elif target < matrix[mid][0]:
                end = mid-1
            elif target > matrix[mid][len(matrix[mid])-1]:
                start = mid+1
        return False