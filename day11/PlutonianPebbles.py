from functools import cache

def splitNumber(number):
    numberStr = str(number)
    midpoint = len(numberStr) // 2
    first = numberStr[:midpoint]
    second = numberStr[midpoint:]
    return first, second

def expand(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        first, second = splitNumber(stone)
        return [int(first), int(second)]
    else:
        return[stone*2024]

@cache
def iterate(stone, iteration):
    if iteration == 0:
        return 1
    stones = expand(stone)
    return sum(iterate(stone, iteration - 1) for stone in stones)


if __name__ == '__main__':
    with open('day11/input.txt', 'r') as file:
        content = file.read()
    stones = list(map(int, content.split()))

    print('stones after 25 iterations:', sum(iterate(stone, 25) for stone in stones))
    print('stones after 75 iterations:', sum(iterate(stone, 75) for stone in stones))
