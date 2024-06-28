from ctypes import c_double, c_int, CDLL
import sys

library = CDLL('./fibonacci.so')
fibonacciC = library.fibonacci
fibonacciC.restype = c_int
