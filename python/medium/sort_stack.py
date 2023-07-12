# sort a stack using only pop, append, and recursion

def sortStack(stack):
    if len(stack) < 2:
        return stack
    b = stack.pop()
    sortStack(stack)
    a = stack.pop()

    larger, smaller = max(a, b), min(a, b)
    stack.append(smaller)
    sortStack(stack)
    stack.append(larger)
    return stack
