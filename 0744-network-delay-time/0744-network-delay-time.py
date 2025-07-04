MAX_VALUE = 1000000
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_matrix = [[-1 for _ in range(n)] for _ in range(n)] 

        k_in_matrix = k - 1

        for time in times:
            source = time[0] - 1 
            target = time[1] - 1
            time_value = time[2]

            adjacency_matrix[source][target] = time_value
            adjacency_matrix[source][source] = 0
            adjacency_matrix[target][target] = 0


        queue = [(k_in_matrix, 0)]
        visited = {}
        print(adjacency_matrix)
        while len(queue):
            current_node, current_node_weight = queue.pop()
            if current_node in visited:
                visited[current_node] = min(current_node_weight, visited[current_node])
            else:
                visited[current_node] = current_node_weight



            for node, node_weight in enumerate(adjacency_matrix[current_node]):
                if node != current_node and node_weight != -1:
                    if node not in visited or (node_weight + current_node_weight < visited[node]):
                        queue.append((node, current_node_weight + node_weight))



        values = []
        for idx, _  in enumerate(adjacency_matrix):
            if idx not in visited:
                return -1
            values.append(visited[idx])

        return max(values)


        