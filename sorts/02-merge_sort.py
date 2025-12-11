'''
merge sort,stable and fast sort but use more Ram space.
'''
import time
import random

def time_merge_sort(array):
    start = time.time()
    sorted_array = merge_sort(array)
    end = time.time()
    
    excution_time = end - start
    print(f"Excution_time = {excution_time: .6f}")
    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

test_array = [random.randint(1,1000) for _ in range(1000)]
print("sorted array =", time_merge_sort(test_array))