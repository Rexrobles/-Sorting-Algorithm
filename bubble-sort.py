# BUBBLE SORT
# - compare two adjacent elements
# - if first element is greater than  second element then Swap
# - if first element is less than second element then leave it as is
# - repeat steps excluding the sorted larger elements in the right part of the array

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39] # unsorted list of numbers

print(f"\nUnsorted Numbers: {numbers}\n")

def sort(numbers):
    for element in range(len(numbers)-1, 0, -1):
        for maxNUM in range(element):
            if numbers[maxNUM]>numbers[maxNUM+1]:
                
                # swapping of numbers
                temp = numbers[maxNUM]
                numbers[maxNUM] = numbers[maxNUM+1]
                numbers[maxNUM+1] = temp
                
        print(numbers) # prints the numbers per loop

    print(f"\nSorted numbers: {numbers}\n") # Printing statement for output.
    
sort(numbers)