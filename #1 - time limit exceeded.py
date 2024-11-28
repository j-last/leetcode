def shortestDistanceAfterQueries(n, queries):
    """
    :type n: int
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    answers = []
    prev_paths = [(n, [i for i in range(n)])]

    min_val = n
    for start_node, end_node in queries:
        for answer, path in prev_paths.copy():
            if start_node in path and end_node in path:
                current = path.copy()
                del current[current.index(start_node)+1 : current.index(end_node)]
                prev_paths.append((len(current), current))
                min_val = min(min_val, len(current)-1)
        answers.append(min_val)
    return answers

print(
    shortestDistanceAfterQueries(4, [[0,3],[0,2]])
)
