# SELECTION SORT
# - Find the smallest number
# - Swap
# - Repeat the steps excluding the arranged elements on the right

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39]

print(f"\nUnsorted Numbers: {numbers}\n")

def sort(numbers):
    for elements in range(9):
        minpos = elements
        
        for minNUM in range (elements,10):
            if numbers[minNUM] <numbers [minpos]:
                minpos = minNUM
            
        #For the array values to swap.
        temp = numbers[elements]
        numbers [elements] = numbers [minpos]
        numbers[minpos] = temp
    
        print(numbers)
    
    print(f"\nSorted numbers: {numbers}\n")
    
sort(numbers)