#采用的递归算法，需要考虑各种边界情况复杂度为mn
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        elif len(matrix)==1:
            return matrix[0]
        else:
            if len(matrix[0])==0:
                return []
            if len(matrix[0])==1:
                return [x[0] for x in matrix]
            result = []
            result = result+matrix[0]
            for i in range(1,len(matrix)-1):
                result.append(matrix[i][-1])
                matrix[i].pop(-1)
            result.extend(matrix[-1][::-1])
            for i in range(1,len(matrix)-1).__reversed__():
                result.append(matrix[i][0])
                matrix[i].pop(0)
            
            result.extend(self.spiralOrder(matrix[1:-1]))
            return result
