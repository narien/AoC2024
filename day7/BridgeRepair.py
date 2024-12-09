from itertools import product

def evaluate(equation, allowConcatenate):
    results = []
    ops = ['+', '*']
    if allowConcatenate:
        ops.append('||')
    operators = list(product(ops, repeat=len(equation)-1))

    for ops in operators:
        current_value = equation[0]
        for i, op in enumerate(ops):
            if op == '+':
                current_value += equation[i+1]
            elif op == '*':
                current_value *= equation[i+1]
            elif op == '||':
                current_value = int(str(current_value) + str(equation[i+1]))
        results.append(current_value)
    return results



def calcTotalCalibrationResult(equations, allowConcatenate):
    total = 0
    for equation in equations:
        if equation[0] in evaluate(equation[1:], allowConcatenate):
            total += equation[0]
    return total

if __name__ == '__main__':
    with open('day7/input.txt', 'r') as file:
        lines = file.readlines()

    equations = []
    for line in lines:
        key, values = line.split(':')

        equation = list(map(int, values.strip().split()))
        equation.insert(0, int(key))
        equations.append(equation)
    print('Total calibration result P1:', calcTotalCalibrationResult(equations, False))
    print('Total calibration result P2:', calcTotalCalibrationResult(equations, True))
