import re


def arithmetic_arranger(problems, display_ans=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_operands = []
    second_operands = []
    operators = []
    for problem in problems:
        try:
            first_operand, operator, second_operand = problem.split(" ")
            if operator not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."

        except:
            if '+' in problem:
                first_operand, second_operand = problem.split('+')
                operator = '+'

            elif '-' in problem:
                first_operand, second_operand = problem.split('-')
                operator = '-'

            else:
                return "Error: Operator must be '+' or '-'."

        first_operand = first_operand.strip()
        second_operand = second_operand.strip()

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        elif re.findall('[^0-9]+', first_operand):
            return "Error: Numbers must only contain digits."


        elif re.findall('[^0-9]+', second_operand):
            return "Error: Numbers must only contain digits."


        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first_operands)):
        if len(first_operands[i]) > len(second_operands[i]):
            first_line.append(" " * 2 + first_operands[i])
        else:
            first_line.append(" " * (len(second_operands[i]) - len(first_operands[i]) + 2) + first_operands[i])

    for i in range(len(second_operands)):
        if len(second_operands[i]) > len(first_operands[i]):
            second_line.append(operators[i] + " " + second_operands[i])
        else:
            second_line.append(
                operators[i] + " " * (len(first_operands[i]) - len(second_operands[i]) + 1) + second_operands[i])

    for i in range(len(first_operands)):
        third_line.append("-" * (max(len(first_operands[i]), len(second_operands[i])) + 2))

    spaces = f'{" "*4}'
    if display_ans:
        for i in range(len(first_operands)):
            if operators[i] == "+":
                ans = str(int(first_operands[i]) + int(second_operands[i]))
            else:
                ans = str(int(first_operands[i]) - int(second_operands[i]))

            if len(ans) > max(len(first_operands[i]), len(second_operands[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" " * (max(len(first_operands[i]), len(second_operands[i])) - len(ans) + 2) + ans)
        arranged_problems = spaces.join(first_line) + "\n" + spaces.join(second_line) + "\n" + spaces.join(
            third_line) + "\n" + spaces.join(fourth_line)
    else:
        arranged_problems = spaces.join(first_line) + "\n" + spaces.join(second_line) + "\n" + spaces.join(third_line)
    return arranged_problems

print(arithmetic_arranger(['201 + 30','200+2', '50 - 14'], display_ans=True))
