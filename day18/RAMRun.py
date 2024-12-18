from collections import deque

def findShortestPath(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start, [start])])  # Queue of tuples (current_position, path)
    visited = set([start])

    while queue:
        (current, path) = queue.popleft()
        if current == goal:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] != '#' and (next_row, next_col) not in visited:
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))
                visited.add((next_row, next_col))

    return None  # No path found

if __name__ == '__main__':
    if True:
        memoryRange = 71
        simulationLimit = 1024
    else:
        memoryRange = 7
        simulationLimit = 12
    coordinates = []
    with open('day18/input.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            tuple_values = (int(values[0]), int(values[1]))
            coordinates.append(tuple_values)

    memory = [['.' for _ in range(memoryRange)] for _ in range(memoryRange)]

    for i in range(simulationLimit):
        memory[coordinates[i][1]][coordinates[i][0]] = '#'
    path = findShortestPath(memory, (0, 0), (memoryRange - 1, memoryRange - 1))
    print('Shortest path length is:', len(path) - 1)

    for i in range(simulationLimit, len(coordinates)):
        memory[coordinates[i][1]][coordinates[i][0]] = '#'
        if (coordinates[i][1], coordinates[i][0]) in path:
            path = findShortestPath(memory, (0, 0), (memoryRange - 1, memoryRange - 1))
        if path == None:
            print(','.join(map(str, coordinates[i])))
            break