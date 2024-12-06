directions = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}
clockwiseTurns = {'v': '<', '^': '>', '<': '^', '>': 'v'}

def copyMatrix(matrix):
    return [row[:] for row in matrix]

def findStart(matrix):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char in directions:
                return y, x, char

def traverse(matrix, start):
    visitedPositions = set()
    y, x, direction = start

    while True:
        dy, dx = directions[direction]
        ny, nx = y + dy, x + dx

        # Exit area
        if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
            matrix[y][x] = 'X'
            break
        # Turn
        if matrix[ny][nx] == '#':
            direction = clockwiseTurns[direction]
        # Step forward
        else:
            if (y, x, direction) in visitedPositions:
                return 0
            visitedPositions.add((y, x, direction))
            matrix[y][x] = 'X'
            y, x = ny, nx
            matrix[y][x] = direction

    count = 0
    for row in matrix:
        count += row.count('X')

    return count


def countPossibleLoops(origMatrix, start):
    lenY = len(origMatrix)
    lenX = len(origMatrix[0])
    count = 0
    for y in range(lenY):
        for x in range(lenX):
            print('evaluating', y, x)
            matrix = copyMatrix(origMatrix)
            if matrix[y][x] == '.':
                matrix[y][x] = '#'
                if not traverse(matrix, start):
                    count += 1
    return count

if __name__ == '__main__':
    with open('day6/input.txt', 'r') as file:
        file_content = file.read()
    matrix = [list(line) for line in file_content.strip().split('\n')]

    start = findStart(matrix)
    print('Distinct places visited:', traverse(copyMatrix(matrix), start))
    print('Possible loops', countPossibleLoops(matrix, start))
