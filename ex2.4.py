import  matplotlib.pyplot as plt
import timeit
import json

import sys
sys.setrecursionlimit(20000)

def dual_pivot_partition(arr, low, high):
    pivot1, pivot2 = arr[low], arr[high]
    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1
        arr[low], arr[high] = arr[high], arr[low]
    i, j = low + 1, high - 1
    k = low + 1
    while k <= j:
        if arr[k] < pivot1:
            arr[k], arr[i] = arr[i], arr[k]
            i += 1
        elif arr[k] >= pivot2:
            while arr[j] > pivot2 and k < j:
                j -= 1
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
            if arr[k] < pivot1:
                arr[k], arr[i] = arr[i], arr[k]
                i += 1
        k += 1
    i -= 1
    j += 1
    arr[low], arr[i] = arr[i], arr[low]
    arr[high], arr[j] = arr[j], arr[high]
    return i, j

def dual_pivot_quick_sort(arr, low, high):
    if low < high:
        pivot1, pivot2 = dual_pivot_partition(arr, low, high)
        dual_pivot_quick_sort(arr, low, pivot1-1)
        dual_pivot_quick_sort(arr, pivot1+1, pivot2-1)
        dual_pivot_quick_sort(arr, pivot2+1, high)

def func1(arr, low, high):
    dual_pivot_quick_sort(arr, low, high)



with open("ex2.json", "r") as in_file:
    data = json.load(in_file)

input_sizes = []
execution_times = []
for input_data in data:
    execution_time = timeit.timeit(lambda: func1(input_data, 0, len(input_data) - 1), number = 1)
    input_sizes.append(len(input_data))
    execution_times.append(execution_time)

plt.plot(input_sizes, execution_times, 'o-')
plt.xlabel("Input Size")
plt.ylabel("Execution Time(seconds)")
plt.title("Modified Quick Sort Algorithm Performance")
plt.show()
