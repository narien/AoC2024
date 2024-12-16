from collections import deque

def findStartAndEnd(matrix):
    start = None
    end = None
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end

def findBestPath(matrix):
    start, end = findStartAndEnd(matrix)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    directionNames = ['up', 'down', 'left', 'right']

    queue = deque([(start, 'left', 0, [start])])
    optimalWay = {}
    completedPaths = []

    while queue:
        (x, y), currentDirection, cost, path = queue.popleft()

        # If we reach the end position
        if (x, y) == end:
            completedPaths.append((cost, path))
            continue

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if (nx, ny) in path:
                continue
            newDirection = directionNames[i]

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != '#':
                newCost = cost + 1
                if newDirection != currentDirection:
                    newCost += 1000
                pos = (nx, ny)
                # if already visited with lower score this path is dead.
                if (pos, newDirection) not in optimalWay or optimalWay[(pos, newDirection)] >= newCost:
                    optimalWay[(pos, newDirection)] = newCost
                    queue.append((pos, newDirection, newCost, path + [pos]))

    winningScore, _ = min(completedPaths, key=lambda x: x[0])
    bestSeats = set()
    for cost, path in completedPaths:
        if cost == winningScore:
            bestSeats.update(path)

    return winningScore, bestSeats

if __name__ == '__main__':
    with open('day16/input.txt', 'r') as file:
        lines = file.readlines()
        matrix = [list(line.strip()) for line in lines]

    least_points, bestSeats = findBestPath(matrix)
    print(f"The least points path from 'S' to 'E' has {least_points} points.")
    print("Number of optimal seats:", len(bestSeats))
