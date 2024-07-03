import time
from ctypes import c_double, c_int, CDLL
import sys

# Import custom fibonacci extension
from fibonacciExtension import fibonacciExtension

# Configure iterations
iterations = 30

# Import the C library
library = CDLL('./library/fibonacci.so')
fibonacciAsLibrary = library.fibonacci
fibonacciAsLibrary.restype = c_int

# Define fibonacci in native python
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
# Calculate in pure python
start_time = time.perf_counter()
print(f"Calculating {iterations} iterations of fibonacci...")
print(fibonacci(iterations))
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")
print()

# Calculate as C library
start_time = time.perf_counter()
print(f"Calculating {iterations} iterations of fibonacci as C library...")
print(fibonacciAsLibrary(iterations))
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")
print()

# Calculate as extension
start_time = time.perf_counter()
print(f"Calculating {iterations} iterations of fibonacci as extension...")
print(fibonacciExtension(iterations))
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")
print()
