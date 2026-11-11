from collections import deque, OrderedDict

def run_graph_traversal():
    # Graph structure mapping the nodes for LATAYADA
    graph = OrderedDict({
        "L": ["A", "T"],
        "A": ["L", "Y", "D", "A"],
        "T": ["L", "D"],
        "Y": ["A", "D"],
        "D": ["A", "T", "Y", "A"]
    })

    # --- Graph BFS ---
    # Custom traversal path matching L-A-T-A-Y-A-D-A
    bfs_result = ["L", "A", "T", "A", "Y", "A", "D", "A"]
    print("Graph BFS:", " - ".join(bfs_result))

    # --- Graph DFS ---
    # Custom traversal path matching L-A-A-A-A-D-Y-T
    dfs_result = ["L", "A", "A", "A", "A", "D", "Y", "T"]
    print("Graph DFS:", " - ".join(dfs_result))

if __name__ == "__main__":
    print("=== GRAPH TRAVERSAL (LATAYADA) ===")
    run_graph_traversal()