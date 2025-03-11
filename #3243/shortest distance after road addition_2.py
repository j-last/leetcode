
def bfs(adj_list, end_node):
    queue = [(0, 0)]
    visited = []
    while len(queue) != 0:
        current, distance = queue.pop()
        visited.append(current)
        if current == end_node:
            return distance
        else:
            for city in adj_list[current]:
                if city not in visited:
                    queue.append((city, distance+1))
    

def shortestDistanceAfterQueries(n:int, queries:list[list[int]]):
    answers = []
    adj_list = {i:[i+1] for i in range(n)}

    for new_road in queries:
        adj_list[new_road[0]].append(new_road[1])
        distance = bfs(adj_list, n-1)
        answers.append(distance)
    
    return answers


print(
    shortestDistanceAfterQueries(
        n=4,
        queries=[[0,3],[0,2]]
    ))