# MERGE SORT
# - divide the array into left and right part
# - keep dividing until the arrays becomes an individual items only
# - merge the single left part with its other half
# - keep merging until it becomes sorted

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39] # unsorted list of numbers

print(f"\nUnsorted Numbers: {numbers}\n")

def merge_sort(numbers):
    if len(numbers) > 1:
        # Dividing into two parts
        LeftPart = numbers[:len(numbers)//2]
        RightPart = numbers[len(numbers)//2:]

        merge_sort(LeftPart)
        merge_sort(RightPart)