def binary_search(array, search_for):
    slice_start = 0
    slice_end = len(l) - 1
    found = False
    location = ''
    while slice_start <= slice_end and not found:
        location = (slice_start + slice_end)
        if array[location] == search_for:
            found = True
        else:
            if search_for < array[location]:
                slice_end = location - 1
            else:
                slice_start = location + 1
    return location

print("\n")
print("=============================")
l = [2, 3, 5, 8, 11, 12, 18]
number = 11
result = binary_search(l, number)

print("Binary Search: number %d found at position %d" % (number, result))
