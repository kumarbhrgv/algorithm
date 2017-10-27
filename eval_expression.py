import re
expression = '12-10+12+1-12'
exp = re.sub("\+"," + ", expression)
exp = re.sub("-"," - ", exp)
stack = exp.split()
stack.reverse()
op1= 0
while len(stack) != 1:
    cursor = stack.pop()
    if cursor in ['+','-']:
        op2= stack.pop()
        if cursor == '+':
            op1 = int(op1)+int(op2)
        elif cursor == '-':
            op1 = int(op1)-int(op2)
        stack.insert(0, op1)
    else:
        op1 = cursor
print(stack.pop())