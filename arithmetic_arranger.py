#define the function
def arithmetic_arranger(problems, show_answer=False):

#check if there are too many problems
if len(problems) > 5:
return "Error: Too many problems."

#initialize the lists to store the lines of output
first_line = []
second_line = []
third_line = []
fourth_line = []

#loop through each problem
for problem in problems:

#split the problem into operands and operator
operand1, operator, operand2 = problem.split()

#check if the operator is valid
if operator not in ["+", "-"]:
return "Error: Operator must be '+' or '-'."

#check if the operands are digits
if not (operand1.isdigit() and operand2.isdigit()):
return "Error: Numbers must only contain digits."

#check if the operands are too long
if len(operand1) > 4 or len(operand2) > 4:
return "Error: Numbers cannot be more than four digits."

#calculate the width of the problem
width = max(len(operand1), len(operand2)) + 2

#format the first line
first_line.append(operand1.rjust(width))

#format the second line
second_line.append(operator + " " + operand2.rjust(width - 2))

#format the third line
third_line.append("-" * width)

#calculate and format the answer if needed
if show_answer:
if operator == "+":
answer = int(operand1) + int(operand2)
else:
answer = int(operand1) - int(operand2)
fourth_line.append(str(answer).rjust(width))

#join the lines with four spaces between each problem
output = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
if show_answer:
output += "\n" + "    ".join(fourth_line)

return the output
return output

#test the function with some examples
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
