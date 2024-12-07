from itertools import product

with open('D07I.txt') as f:
    equations = f.read().splitlines()

def calc(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '|':
            result = result * 10 ** len(str(numbers[i+1])) + numbers[i + 1]
    return result

def check(target, numbers):
    if len(numbers) == 1:
        return numbers[0] == target

    operator_combinations = product('+*|', repeat=len(numbers) - 1)
    for operators in operator_combinations:
        if calc(numbers, operators) == target:
            return True
    return False

def read(eq):
    total = 0
    for equation in eq:
        target, numbers = equation.split(': ')
        target = int(target)
        numbers = tuple(map(int, numbers.split()))
        if check(target, numbers):
            total += target
    return total

r = read(equations)
print(r)
