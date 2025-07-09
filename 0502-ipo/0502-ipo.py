import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
      projects_heap = []

      for i in range(len(capital)):
       heapq.heappush(projects_heap, (-profits[i], capital[i]))

      current_k = 0
      initial_capital = w
      result = w

      return_to_heap = []
      while current_k != k and len(projects_heap):
        current_profit, current_capital = heapq.heappop(projects_heap)
  
        if current_capital <= initial_capital:
          current_k+=1
          result+= -current_profit
          initial_capital+= -current_profit

          while len(return_to_heap):
            heapq.heappush(projects_heap, return_to_heap.pop())
        else:
          return_to_heap.append((current_profit, current_capital))


      return result

        