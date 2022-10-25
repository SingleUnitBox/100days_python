from flask import Flask
import random


# app = Flask(__name__)
#
# print(random.__name__)
# print(__name__)


# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()

import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        end_time = time.time()
        return end_time - current_time
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

print(fast_function())
print(slow_function())
