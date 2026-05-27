import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    negative_heap = []
    for num in nums:
        heapq.heappush(negative_heap, -num)
        
    sorted_heap = []
    while negative_heap:
        sorted_heap.append(-heapq.heappop(negative_heap))
    return sorted_heap

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
