"""
    Scope of variables:
        1) Local
        2) Enclosing
        3) GLobal
        4) Built-in
"""


#global keyword
# x = 30

# def changeGlobal():
#     global x
#     x += 20
#     return x

# print(f"Function variable x will be {changeGlobal()}")
# print(f"global variable x will be {x}")





#non local keyword
# def fnc():
#     x = 20
#     def changeX():
#         nonlocal x 
#         x = 10
#         return x
#     changeX()
#     return x

# print(f"X is {fnc()}")
