import random

# random numbers for sorting
unsorted = random.sample(range(1, 100), 50)

# sort function
def selection_sort(arr):
    index = 0
    min_index = 0
    while index < len(arr):
        # find position of next smallest number
        for x in range(index, len(arr)):
            if arr[x] < arr[min_index]:
                min_index = x

        #swap
        temp = arr[index]
        arr[index] = arr[min_index]
        arr[min_index] = temp
        index += 1

print(unsorted)
selection_sort(unsorted)
print(unsorted)
