# QUICK SORT
# choose any element as pivot
# move the pivot to the end of array
# look for itemFromLeft that is larger than pivot
# look for itemFromRight that is smaller than pivot
# swap the item from left to item from right
# Repeat the process, stop when index of itemFromLeft is greater than index of itemFromRight
# Swap the pivot with itemFromLeft
# repeat until all element are sorted

numbers = [96, 20, 67, 27, 38, 7, 33, 43, 21, 39] # unsorted list of numbers

print(f"\nUnsorted Numbers: {numbers}\n")