# August-22-2023

from typing import Dict, List


class Solution:
    def __init__(self, graph: Dict[int, List[int]]):
        self.graph = graph
        self.visited_list: List[bool] = [False] * (len(self.graph) + 1)
        self.traversal_order: List[int] = []
        self.queue: List[int] = []

    def bfs(self, node: int) -> List[int]:
        self.visited_list[node] = True
        self.queue.append(node)
        self.traversal_order.append(node)

        while self.queue:
            vertex = self.queue.pop(0)
            for node in self.graph[vertex]:
                if not self.visited_list[node]:
                    self.visited_list[node] = True
                    self.traversal_order.append(node)
                    self.queue.append(node)
        return self.traversal_order


# Example to call the BFS function
# graph: Dict[int, List[int]] = {
#     1: [2,3],
#     2: [4,5,1],
#     3: [6,7],
#     4: [2],
#     5: [2],
#     6: [3],
#     7: [3],
# }
# starting_node = 2
#
# s = Solution(graph)
# print(s.bfs(starting_node))
# YouTube: https://www.youtube.com/watch?v=-tgVpUgsQ5k&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
