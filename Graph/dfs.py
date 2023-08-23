# August-22-2023

from typing import Dict, List


class Solution:
    def __init__(self, graph: Dict[int, List[int]]):
        self.graph = graph
        self.visited_list: List[bool] = [False] * (len(self.graph) + 1)
        self.traversal_order: List[int] = []

    def dfs(self, node: int) -> List[int]:
        self.visited_list[node] = True
        self.traversal_order.append(node)
        for connected_node in self.graph[node]:
            if not self.visited_list[connected_node]:
                self.dfs(connected_node)
        return self.traversal_order


# Example to call the DFS function
# graph: Dict[int, List[int]] = {
#     1: [2],
#     2: [1, 3, 5, 4],
#     3: [2, 4],
#     4: [2, 3, 5],
#     5: [2, 4],
#     6: [7],
#     7: [6],
# }
# starting_node = 2
#
# s = Solution(graph)
# print(s.dfs(starting_node))
# YouTube: https://www.youtube.com/watch?v=Qzf1a--rhp8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
