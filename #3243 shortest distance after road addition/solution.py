from math import inf

def dijkstras(adj_list):

    weights = [i for i in range(len(adj_list))]
    visited = []
    to_visit = [0]
    current = None

    while to_visit != []:
        current = to_visit.pop(0)
        visited.append(current)
        for adj_node in adj_list[current]:
            weights[adj_node] = min(weights[adj_node], weights[current] + 1)
            if adj_node not in visited + to_visit:
                to_visit += [adj_node]

    return weights[-1]

def shortestDistanceAfterQueries(n, queries):
    """
    :type n: int
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    answers = []
    adj_list = {i:[i+1] for i in range(n-1)}
    adj_list[n-1] = []

    for start_node, end_node in queries:
        adj_list[start_node] += [end_node]
        answers.append(dijkstras(adj_list))
    return answers

print(
    shortestDistanceAfterQueries(5, [[0,2],[0,4]])
)
