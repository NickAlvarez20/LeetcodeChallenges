import heapq


data = [10, 5, 20, 1]
heapq.heapify(data) # data is now [1,5,20,10]
heapq.heappush(data, 3) # Adds 4 and maintains heap order
smallest = heapq.heappop(data) # Returns 1

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)

    def _bubble_up(self, index):
        parent = (index-1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def pop(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()

        root = self.heap[0]
        self._bubble_down(0)
        return root

    def _bubble_down(self, index):
        smallest = index
        left, right = 2 * index + 1, 2 * index + 2
        # Find the smallest among parent and children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)