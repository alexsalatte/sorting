import random

unsorted = random.sample(range(1,100), 50)

def insertion_sort(arr):
    index = 1
    while index < len(arr):
        previous = index - 1
        temp = arr[index]
        
        while previous >= 0 and arr[previous] > temp:
            arr[previous + 1] = arr[previous]
            previous -= 1
        arr[previous + 1] = temp
        index += 1

print(unsorted)
insertion_sort(unsorted)
print(unsorted)
