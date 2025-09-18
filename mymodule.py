"""
    It is a module that contains 4 calculation functions.
"""

import random
import math

def sum( *args ):
    result = 0
    for n in args:
        result += n
    return result


def multiple( *args ):
    result = 0
    for n in args:
        multiple *= n
    return result

def divide(a , b):
    return a/b


def sqrt(a):
    answer = math.sqrt(a)
    return answer


def randomNumber():
    n = random.randrange(1, 11)
    return n