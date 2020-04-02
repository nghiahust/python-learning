""" This script compute the sum of the facotrial of a list of numbers"""
import math
from multiply import list_product


def compute(numbers):
    return([math.factorial(n) for n in numbers])

l = [1, 2, 3, 4, 5, 6]
print(list_product(l))