'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
def spiral_traversal(matrix):
    i, j = 0, 0
    left = top = 0
    path = []
    
    try:
        bot, right = len(matrix), len(matrix[0])
    except:
        return []
    
    dir_right = 0
    dir_down = 1
    dir_left = 2
    dir_up = 3
    
    d = dir_right
    while left < right and top < bot:
        path.append(matrix[i][j])
        if d == dir_right:
            if j + 1 <= right - 1:
                j += 1
            else:
                d = dir_down
                i += 1
                top += 1
        elif d == dir_down:
            if i + 1 <= bot - 1:
                i += 1
            else:
                d = dir_left
                j -= 1
                right -= 1
        elif d == dir_left:
            if j - 1 >= left:
                j -= 1
            else:
                d = dir_up
                i -= 1
                bot -= 1
        else:
            if i - 1 >= top:
                i -= 1
            else:
                d = dir_right
                j += 1
                left += 1
    return path

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(spiral_traversal(matrix))