import re

def calculateAllMul(content):
    pattern = r"mul\((\d+),(\d+)\)"
    Pairs = re.findall(pattern, content)
    Products = [(int(x) * int(y)) for x, y in Pairs]
    totalSum = sum(Products)

    print('Sum of all mul:', totalSum)

def calculateOnlyDoMul(content):
    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"
    mulPattern = r"mul\((\d+),(\d+)\)"

    doState = True
    sum = 0

    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", content)
    for token in tokens:
        if re.match(doPattern, token):
            doState = True
        elif re.match(dontPattern, token):
            doState = False
        elif re.match(mulPattern, token):
            if doState:
                x, y = map(int, re.findall(r"\d+", token))
                sum += x * y

    print('Sum of all do mul:', sum)


if __name__ == '__main__':
    with open('day3/input.txt', 'r') as file:
        content = file.read()

    calculateAllMul(content)
    calculateOnlyDoMul(content)
