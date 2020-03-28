#!/usr/bin/env python
numbers = [5, 1, 8, 3, 2]

def bubble_sort(arr):
    original = arr
    n = len(arr)

    for i in range(n):
        nr = n - i - 1
        for j in range(0, nr):
            if arr[j] > arr[j+1] :
                temp = arr[j]
                #arr[j], arr[j+1] = arr[j+1], arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print("=============================")
print("Buble sort")
print(bubble_sort(numbers))


