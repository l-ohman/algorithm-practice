# https://leetcode.com/problems/evaluate-reverse-polish-notation
from math import ceil, floor, trunc

def evalRPN(tokens):
    stack = []
    for token in tokens:
        value = 0
        if token == "+":
            value = stack.pop() + stack.pop()
        elif token == "-":
            value = -stack.pop() + stack.pop()
        elif token == "*":
            value = stack.pop() * stack.pop()
        elif token == "/":
            value = 1/stack.pop() * stack.pop()
            value = ceil(value) if value < 0 else floor(
                value)  # must truncate towards 0
            # turns out there's a function for this - `math.trunc`
        else:
            value = int(token)
        stack.append(value)
    return stack[0]

# reordered solution, a bit cleaner
def evalRPN(tokens):
    operators = {"+", "-", "*", "/"}
    stack = []
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            num2, num1 = stack.pop(), stack.pop()
            if token == "+":
                stack.append(num1+num2)
            elif token == "-":
                stack.append(num1-num2)
            elif token == "*":
                stack.append(num1*num2)
            elif token == "/":
                stack.append(trunc(num1/num2))
    return stack[0]

print(evalRPN(["2","1","+","3","*"])==9)
print(evalRPN(["4","13","5","/","+"])==6)
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])==22)
print(evalRPN(["4","-2","/","2","-3","-","-"])==-7)
