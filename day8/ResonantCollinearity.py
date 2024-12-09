def findAntiNodes(matrix, yOrig, xOrig, generateResonant):
    def between(value, lower, upper):
        return lower < value < upper
    def generateResonants(yLower, yUpper, xLower, xUpper, y, x, yDelta, xDelta, antiNodes):
        while between(y, yLower, yUpper) and between(x, xLower, xUpper):
            antiNodes.append((y, x))
            y += yDelta
            x += xDelta

    antiNodes = []
    yLower, yUpper, xLower, xUpper = -1, len(matrix), -1, len(matrix[0])
    signal = matrix[yOrig][xOrig]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if y == yOrig and x == xOrig:
                continue
            if matrix[y][x] == signal:
                yDelta, xDelta = y - yOrig, x - xOrig
                if generateResonant:
                    generateResonants(yLower, yUpper, xLower, xUpper, y, x, yDelta, xDelta, antiNodes)
                else:
                    if between(y + yDelta, yLower, yUpper) and between(x + xDelta, xLower, xUpper):
                        antiNodes.append((y + yDelta, x + xDelta))
    return antiNodes

def countAntiNodes(matrix, generateResonant):
    uniqueLocations = set()

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if not matrix[y][x] == '.':
                uniqueLocations.update(findAntiNodes(matrix, y, x, generateResonant))
    return len(uniqueLocations)

if __name__ == '__main__':
    with open('day8/input.txt', 'r') as file:
        lines = file.readlines()
        matrix = [list(line.strip()) for line in lines]
    
    print('unique anti node locations:', countAntiNodes(matrix, False))
    print('unique anti node locations with resonant harmonics:', countAntiNodes(matrix, True))