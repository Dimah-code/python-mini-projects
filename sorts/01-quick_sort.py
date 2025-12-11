'''
quick sort algorithm for learning how does it work
'''
import time
import random

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    random_number = random.choice(array)
    
    lower = [i for i in array if i < random_number]
    equal = [i for i in array if i == random_number]
    higher = [i for i in array if i > random_number]
    
    return quick_sort(lower) + equal + quick_sort(higher)

def time_quick_sort(array):
    start = time.time()
    result = quick_sort(array)
    end = time.time()
    
    to_take = end - start
    print(f"Execution time = {to_take: .6f} seconds")
    return result


test_array = [random.randint(1,1000) for _ in range(1000)]
sorted_array = time_quick_sort(test_array)
print("sorted array =", sorted_array)