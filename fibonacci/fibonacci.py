import time
from fibonacciWrapper import fibonacciC

iterations = 30

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
# Calculate in pure python
start_time = time.perf_counter()
print("Calculating {iterations} iterations of fibonacci...")
print(fibonacci(iterations))
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")
print()

# Calculate in C
start_time = time.perf_counter()
print("Calculating {iterations} iterations of fibonacci in C...")
print(fibonacciC(iterations))
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")
print()
