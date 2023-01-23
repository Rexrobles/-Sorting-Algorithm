# QUICK SORT
# choose any element as pivot
# move the pivot to the end of array
# look for itemFromLeft that is larger than pivot
# look for itemFromRight that is smaller than pivot
# swap the itemfromleft to itemfromright
# Repeat the process, stop when index of itemFromLeft is greater than index of itemFromRight
# Swap the pivot with itemFromLeft
# repeat until all element are sorted

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39] # unsorted list of numbers

print(f"\nUnsorted Numbers: {numbers}\n")

def quick_sort(numbers,left,right):
    if left < right:
        partition_pos = partition(numbers,left,right)
        quick_sort(numbers, left,  partition_pos - 1)
        quick_sort(numbers, partition_pos + 1, right)
        
def partition(numbers, left, right):
    leftindex = left
    rightindex = right - 1
    pivot = numbers[right]
    
    while leftindex < rightindex:
        while leftindex < right and numbers[leftindex] < pivot:
            leftindex += 1
        while rightindex > left and numbers[rightindex] >= pivot:
            rightindex -=1

        if leftindex < rightindex:
            numbers[leftindex], numbers[rightindex] = numbers[rightindex], numbers[leftindex]

    if numbers[leftindex] > pivot:
        numbers[leftindex], numbers[right] = numbers[right], numbers[leftindex]
    return leftindex