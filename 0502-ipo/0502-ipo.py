import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # with two heaps
        affordable_projects_heap = []  # max heap with affordable projects
        projects_capital_heap = []  # min heap with projects by capital

        for i in range(len(capital)):
            heapq.heappush(projects_capital_heap, (capital[i], profits[i]))

        current_k = 0
        current_capital = w

        for _ in range(k):
            while (
                projects_capital_heap and projects_capital_heap[0][0] <= current_capital
            ):
                current_project = heapq.heappop(projects_capital_heap)
                heapq.heappush(affordable_projects_heap, -current_project[1])

            if affordable_projects_heap:
                current_capital += -(heapq.heappop(affordable_projects_heap))

        return current_capital
