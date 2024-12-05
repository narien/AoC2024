def checkPageOrder(page, update, pairs):
    for value in update:
        dependencies = [second for first, second in pairs if first in update]
        if page in dependencies:
            return False
    return True

def checkUpdateOrder(update, pairs):
    uCopy = update.copy()
    while uCopy:
        page = uCopy.pop(0)
        if not checkPageOrder(page, uCopy, pairs):
            return False
    return True

def customSort(update, pairs):
    while not checkUpdateOrder(update, pairs):
        order = {x: i for i, x in enumerate(update)}
        for first, second in pairs:
            if first in order and second in order:
                if order[first] > order[second]:
                    order[first], order[second] = order[second], order[first]
        update = sorted(update, key=lambda x: order[x])
    return update

def fixPageOrder(update, pairs):
    update = customSort(update, pairs)
    return update[len(update) // 2]

def evaluateUpdates(updates, pairs):
    ValidChecksum = 0
    fixedChecksum = 0
    for update in updates:
        if checkUpdateOrder(update, pairs):
            ValidChecksum += update[len(update) // 2]
        else:
            fixedChecksum += fixPageOrder(update, pairs)
    return ValidChecksum, fixedChecksum

if __name__ == '__main__':
    with open('day5/input.txt', 'r') as file:
        content = file.read().strip()

    pairPart, updatePart = content.split("\n\n")
    pairs = [tuple(map(int, line.split('|'))) for line in pairPart.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updatePart.split('\n')]

    print("Pairs:", pairs)
    print("Updates:", updates)

    validChecksum, fixedChecksum = evaluateUpdates(updates, pairs)
    print("valid checksum:", validChecksum)
    print("fixed checksum:", fixedChecksum)
