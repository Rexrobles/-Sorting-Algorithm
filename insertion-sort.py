# INSERTION SORT
# - consider first element is sorted and the rest is unsorted
# - pick the first element in the unsorted part and place it in its correction position in the sorted part
# - repeat the steps

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39] # unsorted list of numbers

print(f"\nUnsorted Numbers: {numbers}\n")

def sort(numbers):
    for element in range(1, len(numbers)):
        sorted_area = element
        while numbers[sorted_area - 1] > numbers[sorted_area] and sorted_area > 0:
            numbers[sorted_area - 1], numbers[sorted_area] =  numbers[sorted_area], numbers[sorted_area - 1]
            sorted_area -= 1
        
        print(numbers)# prints the numbers per loop
    print(f"\nSorted numbers: {numbers}\n")

sort(numbers)
