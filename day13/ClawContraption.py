import re
import numpy as np

def solve_equation(buttonA, buttonB, answer, compensation):
    A = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])
    B = np.array([answer[0] + compensation, answer[1] + compensation])
    R = np.linalg.solve(A, B).round()
    return int([3, 1] @ R if all(A @ R == B) else 0)

def calcTotalTokenCost(buttons, prizes, compensation):
    totalCost = 0
    for buttonPair, prize in zip(buttons, prizes):
        totalCost += solve_equation(buttonPair[0], buttonPair[1], prize, compensation)
    return totalCost

if __name__ == '__main__':
    buttons = []
    prizes = []

    with open('day13/input.txt', 'r') as file:
        content = file.read()

    # Split the content into sections for each button and prize set
    sections = content.split("\n\n")

    for section in sections:
        lines = section.split("\n")
        button_a = list(map(int, re.findall(r"\d+", lines[0])))
        button_b = list(map(int, re.findall(r"\d+", lines[1])))
        prize = list(map(int, re.findall(r"\d+", lines[2])))

        buttons.append((button_a, button_b))
        prizes.append(prize)
    print('Total cost of tokens p1:', calcTotalTokenCost(buttons, prizes, 0))
    print('Total cost of tokens p2:', calcTotalTokenCost(buttons, prizes, 10000000000000))
