# SELECTION SORT
# - Find the smallest number
# - Swap
# - Repeat the steps excluding the arranged elements on the right

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39]

print(f"\nUnsorted Numbers: {numbers}")

def sort(numbers):
    for elements in range(9):
        minpos = elements
    for minNUM in range (elements,11):
        if numbers[minNUM] <numbers [minpos]:
            minpos = minNUM