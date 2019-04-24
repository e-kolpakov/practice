from collections import namedtuple, defaultdict, deque

Edge = namedtuple("Edge", ["label", "weight", "connected_to"])
ExpansionStep = namedtuple("ExpansionStep", ["vertex", "visited"])

class Graph:
    def __init__(self):
        self._vertices = {}

    def add_vertex(self, label, weight):
        edge = Edge(label, weight, set())
        self._vertices[label] = edge

    def add_edge(self, from_vertex, to_vertex):
        self._vertices[from_vertex].connected_to.add(to_vertex)

    # for the speed of implementation this method intentionally "corrupts" original graph state
    # Since there were no explicit requirement to support running multiple queries against the same graph
    # this is an affordable "tech debt"
    def find_optimal_path_from_vertex(self, vertex_label):
        max_paths = defaultdict(int)
        # use of more efficient data structures for expansion_frontier (e.g. fibbonacci heap)
        # will improve the time complexity) - but for simplicity I'll just use the deque for now
        expansion_frontier = deque()

        start_vertex = self._vertices[vertex_label]
        max_paths[start_vertex.label] = start_vertex.weight

        expansion_frontier.appendleft(ExpansionStep(start_vertex.label, [start_vertex.label]))

        while expansion_frontier:
            step = expansion_frontier.pop()
            current_vertex_label, path = step.vertex, step.visited
            current_vertex = self._vertices[current_vertex_label]
            max_path_to_current = max_paths[current_vertex_label]

            for next_vertex_label in current_vertex.connected_to:
                if next_vertex_label in path:
                    raise Exception(f"Cycle detected: {path + [next_vertex_label]}")

                next_vertex = self._vertices[next_vertex_label]
                new_weight = max_path_to_current + next_vertex.weight

                if new_weight > max_paths[next_vertex_label]:
                    max_paths[next_vertex_label] = new_weight
                    expansion_frontier.appendleft(ExpansionStep(next_vertex.label, path + [next_vertex.label]))

        return max(max_paths.values())


if __name__ == "__main__":
    # Since the input example is malformed (there are no indication how many edges and vertices are there
    # and what is the starting vertex) and "parsing" from the input is demonstrated in the first problem,
    # I'll take a shortcut and just create the graph directly
    graph = Graph()
    graph.add_vertex("A", 1)
    graph.add_vertex("B", 2)
    graph.add_vertex("C", 2)

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("A", "C")
    # graph.add_edge("C", "A")  # uncomment to see cycle detection in action

    start_vertex = "A"
    actual_path_length = graph.find_optimal_path_from_vertex(start_vertex)
    expected_path_length = 5

    assert actual_path_length == 5, f"optimal path should be {expected_path_length}, but was {actual_path_length}"
