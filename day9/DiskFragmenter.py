def writeSegment(disk, length, id):
    for _ in range(length):
        disk.append(id)

def createDisk(input):
    disk = []
    fileId = 0
    isFile = True
    for c in line:
        length = int(c)
        if isFile:
            writeSegment(disk, length, fileId)
            isFile = False
            fileId += 1
        else:
            writeSegment(disk, length, None)
            isFile = True
    return disk

def calcFileChecksum(disk):
    return sum(index * value for index, value in enumerate(disk) if value is not None)

def fragmentDisk(diskOrig):
    disk = diskOrig.copy()
    nextFillIndex = 0
    nextMoveIndex = len(disk) - 1
    def findNextNone(nextFillIndex, disk):
        while nextFillIndex < len(disk) and not disk[nextFillIndex] == None:
            nextFillIndex += 1
        return nextFillIndex
    def findNextMove(nextMoveIndex, disk):
        while nextMoveIndex > 0 and disk[nextMoveIndex] == None:
            nextMoveIndex -= 1
        return nextMoveIndex

    while nextFillIndex < nextMoveIndex:
        nextFillIndex = findNextNone(nextFillIndex, disk)
        nextMoveIndex = findNextMove(nextMoveIndex, disk)
        if nextFillIndex >= nextMoveIndex:
            break
        disk[nextFillIndex] = disk[nextMoveIndex]
        disk[nextMoveIndex] = None
    return calcFileChecksum(disk)

def defragmentDisk(disk):
    nextMoveIndex = len(disk) - 1
    length = 0

    def findNextMove(nextMoveIndex, disk):
        length = 0
        while nextMoveIndex > 0 and disk[nextMoveIndex] == None:
            nextMoveIndex -= 1
        fileId = disk[nextMoveIndex]

        while nextMoveIndex - length > 0 and disk[nextMoveIndex - length] == fileId:
            length += 1
        return nextMoveIndex, length
    def findFillIndex(length, disk):
        index = 0
        max = len(disk)
        currentLength = 0
        while index < max:
            if disk[index] == None:
                currentLength += 1
                if currentLength == length:
                    break
            else:
                currentLength = 0
            index += 1
        return index

    while nextMoveIndex - length > 0:
        nextMoveIndex, length = findNextMove(nextMoveIndex, disk)
        fillIndex = findFillIndex(length, disk)
        if fillIndex >= nextMoveIndex:
            nextMoveIndex -= length
            continue

        for _ in range(length):
            disk[fillIndex] = disk[nextMoveIndex]
            disk[nextMoveIndex] = None
            fillIndex -= 1
            nextMoveIndex -=1

    return calcFileChecksum(disk)


if __name__ == '__main__':
    with open('day9/input.txt', 'r') as file:
        line = file.readline().strip()
    disk = createDisk(line)
    print('fragmentation checksum:', fragmentDisk(disk))
    print('defragmentation checksum:', defragmentDisk(disk))
