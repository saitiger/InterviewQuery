# Solution 1 Using Sorting 
def list_fifths(numlists):
    fifth_largest_list = [sorted(sublist)[-5] for sublist in numlists]
    return sorted(fifth_largest_list)

# Solution 2 Using Heap
import heapq
def list_fifths(numlists):
    fifth_largest_list = []
    for sublist in numlists:
        heap = []
        for num in sublist:
            heapq.heappush(heap, num)
            if len(heap) > 5:
                heapq.heappop(heap)
        fifth_largest_list.append(heap[0])
    return sorted(fifth_largest_list)
