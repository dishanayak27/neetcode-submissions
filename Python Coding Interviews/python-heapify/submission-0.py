import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    output = strings.copy()
    heapq.heapify(output)
    return output


def heapify_integers(integers: List[int]) -> List[int]:
    output = integers.copy()
    heapq.heapify(output)
    return output


def heap_sort(nums: List[int]) -> List[int]:
    heap = nums.copy()
    heapq.heapify(heap)
    
    output=[]
    while heap:
        output.append(heapq.heappop(heap))
    return output


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
