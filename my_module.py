""" This script compute the sum of the facotrial of a list of numbers"""
import math


def compute(numbers):
    return([math.factorial(n) for n in numbers])