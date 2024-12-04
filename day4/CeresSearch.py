def countWord(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    wordLen = len(word)
    count = 0

    # Directions: right, down, diagonal down-right, diagonal down-left
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    def isValid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def searchFrom(x, y, dx, dy):
        for k in range(wordLen):
            nx, ny = x + k * dx, y + k * dy
            if not isValid(nx, ny) or matrix[nx][ny] != word[k]:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            c = matrix[i][j]
            if matrix[i][j] == word[0]:
                for dx, dy in directions:
                    if searchFrom(i, j, dx, dy):
                        count += 1
    return count

def countXShapedMas(matrix):
    count = 0

    def checkXShape(x, y):
        patterns = [
            ('M', 'M', 'S', 'S'),
            ('M', 'S', 'M', 'S'),
            ('S', 'M', 'S', 'M'),
            ('S', 'S', 'M', 'M'),
        ]

        actual = (matrix[x-1][y-1], matrix[x+1][y-1], matrix[x-1][y+1], matrix[x+1][y+1])
        if actual in patterns:
            return True
        return False

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 'A':
                if checkXShape(i, j):
                    count += 1

    return count


if __name__ == '__main__':
    with open('day4/input.txt', 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]

    total = countWord(matrix, 'XMAS')
    total += countWord(matrix, 'SAMX')
    print('Total count of xmas in all directions:', total)
    print('Total count of x shaped mas:', countXShapedMas(matrix))
