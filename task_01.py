"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. 
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq

class MinHeap:
    def __init__(self, arr):
        self.heap = []
        if type(arr) is list: 
            self.heap = arr.copy() 
            for i in range(len(self.heap))[::-1]:  
                self._siftdown(i)  

    def _siftdown(self, i):
        left = 2*i + 1  
        right = 2*i + 2 
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest  
            left = 2*i + 1  
            right = 2*i + 2  

    def extract_min(self):
        if len(self.heap) == 0:  
            return None 
        minval = self.heap[0]  
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  
        self.heap.pop() 
        self._siftdown(0)  
        return minval  


if __name__ == '__main__':

    # Using heapq:

    # pipes = [4, 10, 3, 5, 1]
    # heapq.heapify(pipes)
    # print("Купа: ", pipes)
    # print("Порядок об'єднання, який мінімізує загальні витрати:")
    # while pipes:
    #     min_elem = heapq.heappop(pipes)
    #     print(min_elem, end="->")
        

    # Using custom Class MinHead:

    pipes = [4, 10, 3, 5, 1]
    min_heap = MinHeap(pipes)
    print("Купа: ", min_heap.heap)
    print("Порядок об'єднання, який мінімізує загальні витрати:")
    while min_heap.heap:
        print(min_heap.extract_min(), end="->")
    





