'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]

Output: [1,2,4,7,5,3,6,8,9]
'''
def diag_traversal(matrix):
    try:
        path = [matrix[0][0]]
        m, n = len(matrix), len(matrix[0])
    except:
        return []
        
    i, j = 0, 0
    isUp = True
    
    while i != m-1 or j != n-1:
        if isUp:
            if i-1 >= 0 and j+1 <= n-1: # OK
                i -= 1
                j += 1
            elif j+1 <= n-1: # Crossing top border
                j += 1
                isUp = False
            else: # Crossing right border
                i += 1
                isUp = False
        else:
            print('val:', matrix[i][j]) 
            if i+1 <= m-1 and j-1 >= 0: # OK
                i += 1
                j -= 1
            elif i+1 <= m-1: # Crossing left border
                i += 1
                isUp = True
            else: # Crossing bottom border
                j += 1
                isUp = True    
        path.append(matrix[i][j])
        
    return path

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(diag_travrsal([]))