import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_k_items = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap_k_items) < self.k:
            heapq.heappush(self.heap_k_items, val)
            return self.heap_k_items[0]
        if val > self.heap_k_items[0]:
            heapq.heappop(self.heap_k_items)
            heapq.heappush(self.heap_k_items, val)
            return self.heap_k_items[0]
        else:
            return self.heap_k_items[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
