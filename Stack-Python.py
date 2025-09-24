#using list for STACK
stack = []

def PushItem(n):
    global stack
    stack.append(n)
    return stack


def PopItem():
    if not isEmpty():
        global stack
        stack.pop()
        return stack
    else:
        return "Stack is Empty"


def isEmpty():
    global stack
    return len(stack) == 0

def PeekItem():
    if not isEmpty():
        global stack
        return stack[-1]
    else:
        return "Stack is Empty"


print(PushItem(2))
print(PushItem(4))
print(PushItem(3))
print(PopItem())
print(PeekItem())