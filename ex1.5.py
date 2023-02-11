import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


def fib(n, memo = {}): 
    if n == 0 or n == 1: 
        return n
    if n in memo: 
        return memo[n] 
    else: 
        memo[n] = fib(n-1, memo) + fib(n-2, memo) 
        return memo[n] 

results_original = []
results_improved = []

for i in range(36):
    time_original = timeit.timeit(lambda: func(i), number=1000)
    results_original.append(time_original)
    
    time_optimized = timeit.timeit(lambda: fib(i), number=1000)
    results_improved.append(time_optimized)

plt.plot(results_original, label='Original')
plt.plot(results_improved, label='Optimized')
plt.legend()
plt.xlabel('Input size (n)')
plt.ylabel('Execution time (s)')
plt.title('Timing of Original vs. Improved Code')
plt.show()