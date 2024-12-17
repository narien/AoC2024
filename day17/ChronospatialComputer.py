registers = {}
program = []
output = []

def dv(operand, registry):
    if operand < 4:
        registers[registry] = registers['A'] // (2 ** operand)
    elif operand == 4:
        registers[registry] = registers['A'] // (2 ** registers['A'])
    elif operand == 5:
        registers[registry] = registers['A'] // (2 ** registers['B'])
    elif operand == 6:
        registers[registry] = registers['A'] // (2 ** registers['C'])

def bxl(operand):
    registers['B'] = registers['B'] ^ operand

def bst(operand):
    if operand < 4:
        registers['B'] = operand % 8
    elif operand == 4:
        registers['B'] = registers['A'] % 8
    elif operand == 5:
        registers['B'] = registers['B'] % 8
    elif operand == 6:
        registers['B'] = registers['C'] % 8

def jnz(operand, instructionPointer):
    if registers['A'] == 0:
        return False, instructionPointer
    return True, operand

def bxc():
    registers['B'] = registers['B'] ^ registers['C']

def out(operand):
    if operand < 4:
        output.append(operand % 8)
    elif operand == 4:
        output.append(registers['A'] % 8)
    elif operand == 5:
        output.append(registers['B'] % 8)
    elif operand == 6:
        output.append(registers['C'] % 8)


def runProgram():
    instructionPointer = 0
    programSize = len(program)
    while instructionPointer < programSize:
        opCode = program[instructionPointer]
        operand = program[instructionPointer + 1]
        if opCode == 0:
            dv(operand, 'A')
            instructionPointer += 2
        elif opCode == 1:
            bxl(operand)
            instructionPointer += 2
        elif opCode == 2:
            bst(operand)
            instructionPointer += 2
        elif opCode == 3:
            didJump, instructionPointer = jnz(operand, instructionPointer)
            if not didJump:
                instructionPointer += 2
        elif opCode == 4:
            bxc()
            instructionPointer += 2
        elif opCode == 5:
            out(operand)
            instructionPointer += 2
        elif opCode == 6:
            dv(operand, 'B')
            instructionPointer += 2
        elif opCode == 7:
            dv(operand, 'C')
            instructionPointer += 2

def findCorrectInitValue():
    global registers
    backupRegisters = registers.copy()
    programString = ",".join(map(str, program))

    initialAValue = 0
    while True:
        registers['A'] = initialAValue
        runProgram()
        if ",".join(map(str, output)) == programString:
            return initialAValue
        initialAValue += 1
        registers = backupRegisters.copy()
        output.clear()


if __name__ == '__main__':
    with open('day17/input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Register"):
                parts = line.split(":")
                key = parts[0][-1:].strip()
                value = int(parts[1].strip())
                registers[key] = value
            elif line.startswith("Program"):
                parts = line.split(":")
                program = list(map(int, parts[1].split(',')))
    backupRegisters = registers.copy()
    runProgram()
    print(",".join(map(str, output)))
    registers = backupRegisters
    print('Lowest initial value of A to output a copy of program is:', findCorrectInitValue())
