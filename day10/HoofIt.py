def find_zeros_in_matrix(matrix):
    zero_positions = {}
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                zero_positions[(i, j)] = 0
    return zero_positions

def count_paths_to_nine(matrix, start, countTops):
    rows, cols = len(matrix), len(matrix[0])
    start_x, start_y = start
    target_value = 9
    topsFound = set()

    def dfs(x, y, current_value):
        if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] != current_value + 1:
            return 0
        if matrix[x][y] == target_value:
            if countTops and (x, y) in topsFound:
                return 0
            else:
                topsFound.add((x, y))
                return 1
        return (dfs(x + 1, y, matrix[x][y]) +
                dfs(x - 1, y, matrix[x][y]) +
                dfs(x, y + 1, matrix[x][y]) +
                dfs(x, y - 1, matrix[x][y]))

    return dfs(start_x, start_y, matrix[start_x][start_y] - 1)

if __name__ == '__main__':
    with open('day10/input.txt', 'r') as file:
        lines = file.readlines()
    matrix = [list(map(int, line.strip())) for line in lines]

    trailHeads = find_zeros_in_matrix(matrix)
    for trail in trailHeads:
        trailHeads[trail] = count_paths_to_nine(matrix, trail, True)
    print('Total tops score:', sum(trailHeads.values()))

    trailHeads = find_zeros_in_matrix(matrix)
    for trail in trailHeads:
        trailHeads[trail] = count_paths_to_nine(matrix, trail, False)
    print('Total trails score:', sum(trailHeads.values()))
