def dfs(graph, start, visited=None):
    """使用深度优先搜索遍历图，返回访问顺序。"""
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    result = dfs(graph, "A")
    print(result)
