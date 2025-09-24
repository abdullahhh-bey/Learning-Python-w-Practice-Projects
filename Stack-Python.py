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
    global stack
    return stack[-1]

