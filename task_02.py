"""
Дано k відсортованих списків цілих чисел. 
Ваше завдання — об'єднати їх у один відсортований список. 
Тепер при виконанні завдання ви повинні використати мінімальну купу 
для ефективного злиття кількох відсортованих списків в один відсортований список. 
Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків 
та повертає відсортований список.
"""

import heapq


def merge_k_lists(lists) -> list:
    min_heap = []
    merged_list = []
    for list in lists:
        for item in list:
            heapq.heappush(min_heap, item)
    while min_heap:
        merged_list.append(heapq.heappop(min_heap))
    
    return merged_list


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
