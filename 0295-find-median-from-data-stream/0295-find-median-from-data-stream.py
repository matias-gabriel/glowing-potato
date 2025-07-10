import heapq
class MedianFinder:

    def __init__(self):
        self.num_of_items = 0
        self.first_half_heap = [] # (max heap) with first half, all items here < any items in second half heap
        self.second_half_heap = []
        # balanced heaps len(min) == len(max) or len(min) - len(max) == 1
        # first [1,0,-1]
        # second [2,4,5,] 

    def addNum(self, num: int) -> None:
        if not self.first_half_heap:
            heapq.heappush(self.first_half_heap, -num)
        elif not self.second_half_heap:
            if num <= - self.first_half_heap[0]:
                first_value = - heapq.heappop(self.first_half_heap)
                heapq.heappush(self.second_half_heap, first_value)
                heapq.heappush(self.first_half_heap, -num)
            else:
                heapq.heappush(self.second_half_heap, num)

        else:
            if num <= - self.first_half_heap[0]:
                heapq.heappush(self.first_half_heap, - num)
            else:
                heapq.heappush(self.second_half_heap, num)

            is_balanced = len(self.first_half_heap) == len(self.second_half_heap) or len(self.first_half_heap) - len(self.second_half_heap) == 1

            if not is_balanced:
                if len(self.first_half_heap) > len(self.second_half_heap):
                    value = - heapq.heappop(self.first_half_heap)
                    heapq.heappush(self.second_half_heap, value)
                
                else:
                    value = heapq.heappop(self.second_half_heap)
                    heapq.heappush(self.first_half_heap, - value)
        self.num_of_items+=1 





    def findMedian(self) -> float:
        if self.num_of_items % 2 == 0:
          return (self.second_half_heap[0] - self.first_half_heap[0]) / 2
        else:
           return - self.first_half_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()