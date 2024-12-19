def canBuildString(targetString, substrings):
    # Create a list to keep track of whether a substring can be formed up to each index
    dp = [False] * (len(targetString) + 1)
    dp[0] = True  # Base case: an empty string can always be formed

    for i in range(1, len(targetString) + 1):
        for substring in substrings:
            if dp[i - len(substring)] and targetString[i - len(substring):i] == substring:
                dp[i] = True
                break

    return dp[len(targetString)]

def countCombinations(targetString, substrings):
    def backtrack(start, path):
        if start == len(targetString):
            result.append(path[:])
            return
        for substring in substrings:
            if targetString.startswith(substring, start):
                path.append(substring)
                backtrack(start + len(substring), path)
                path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == '__main__':
    with open('day19/input.txt', 'r') as file:
        lines = file.readlines()

    towelTypes = set(lines[0].strip().split(', '))
    patterns = [line.strip() for line in lines[2:]]

    validPatterns = 0
    for pattern in patterns:
        if canBuildString(pattern, towelTypes):
            validPatterns += 1
    print('Number of valid patterns:', validPatterns)

    totalCombinations = 0
    counter = 0
    for pattern in patterns:
        print(counter)
        counter += 1
        totalCombinations += len(countCombinations(pattern, towelTypes))
    print('Total number of combinations:', totalCombinations)