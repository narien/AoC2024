def findPatches(matrix):
    def dfs(x, y, char, currRegion):
        def countCorners(x, y):
            def isSame(x, y):
                if (x, y) in currRegion:
                    return True
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                    return False
                return char == matrix[x][y]

            corners = 0
            # Upper left
            if not isSame(x - 1, y) and not isSame(x, y - 1):
                corners += 1
            # Upper right
            if not isSame(x - 1, y) and not isSame(x, y + 1):
                corners += 1
            # Lower left
            if not isSame(x + 1, y) and not isSame(x, y - 1):
                corners += 1
            # Lower right
            if not isSame(x + 1, y) and not isSame(x, y + 1):
                corners += 1

            # Upper left
            if not isSame(x-1, y-1) and isSame(x - 1, y) and isSame(x, y - 1):
                corners += 1
            # Upper right
            if not isSame(x-1, y+1) and isSame(x - 1, y) and isSame(x, y + 1):
                corners += 1
            # Lower left
            if not isSame(x + 1, y - 1) and isSame(x + 1, y) and isSame(x, y - 1):
                corners += 1
            # Lower right
            if not isSame(x+1, y+1) and isSame(x + 1, y) and isSame(x, y + 1):
                corners += 1
            return corners

        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != char:
            return 0, 0
        matrix[x][y] = None  # Mark the cell as visited
        size = 1
        perimeter = 0
        corners = countCorners(x, y)
        currRegion.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == char:
                s, p, c = dfs(nx, ny, char, currRegion)
                size += s
                perimeter += p
                corners += c
            elif (nx, ny) not in currRegion:
                perimeter += 1
        return size, perimeter, corners

    patches = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is not None:
                char = matrix[i][j]
                currRegion = set()
                size, perimeter, corners = dfs(i, j, char, currRegion)
                patches.append((char, size, perimeter, corners))
    return patches

if __name__ == '__main__':
    matrix = []
    with open('day12/input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    patches = findPatches(matrix)
    print(patches)
    print('Total price of fencing:', sum(x * y for _, x, y, _ in patches))
    print('Total price with discount:', sum(x * y for _, x, _, y in patches))

