ops = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '^': float.__pow__,
}
def postfix(expression):
    stack = []
    for x in expression.split():
        if x in ops:
            x = ops[x](stack.pop(-2), stack.pop(-1))
        else:
            x = float(x)
        stack.append(x)
    return stack.pop()

def infix(expression):
    stack = []
    for x in expression.split():
        if x in ops:
            stack.append("("+stack.pop(-2)+x+stack.pop(-1)+")")
        else:
            stack.append(x)
    return stack
print(postfix('1 2 + 4 3 - + 10 5 / *'))
print(infix('1 2 + 4 3 - + 10 5 / *'))
