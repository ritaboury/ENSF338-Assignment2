import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", "r") as in_file:
    data = json.load(in_file)

input_sizes = []
execution_times = []
for input_data in data:
    execution_time = timeit.timeit(lambda: func1(input_data, 0, len(input_data) - 1), number=1)
    input_sizes.append(len(input_data))
    execution_times.append(execution_time)

plt.plot(input_sizes, execution_times, 'o-')
plt.xlabel("Input Size")
plt.ylabel("Execution Time(seconds)")
plt.title("Quick Sort Algorithm Performance")
plt.show()
