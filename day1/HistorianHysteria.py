def calcTotalDistance(listA, listB):
    listA.sort()
    listB.sort()

    total = 0
    for a, b in zip(listA, listB):
        total += abs(a-b)

    print("Total distance: ", total)

def calcSimilarityScore(listA, listB):
    total = 0
    for val in listA:
        total += val * listB.count(val)

    print("Similarity score: ", total)

if __name__ == '__main__':
# Initialize two empty lists
    listA = []
    listB = []

    with open('day1/input.txt', 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            listA.append(num1)
            listB.append(num2)

    calcTotalDistance(listA, listB)
    calcSimilarityScore(listA, listB)
