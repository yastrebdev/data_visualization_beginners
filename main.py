import heapq


def dijkstra_shortest_path(city_map, start, goal):
    queue = [(0, start, [])]
    distances = {node: float('inf') for node in city_map}
    distances[start] = 0
    visited = set()

    while queue:
        current_distance, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, current_distance

        for neighbor, distance in city_map[node].items():
            if neighbor not in visited:
                old_cost = distances[neighbor]
                new_cost = current_distance + distance

                if new_cost < old_cost:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor, path))

    return float('inf'), None

city_map = {
    'Home': {'Park': 2, 'School': 5, 'Mail': 10},
    'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
    'School': {'Home': 5, 'Library': 6, 'Mail': 2},
    'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
    'Library': {'School': 6, 'Hospital': 1},
    'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
    'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
    'Museum': {'Park': 4, 'Shop': 5},
    'Shop': {'Museum': 5, 'Theater': 1},
    'Theater': {'Shop': 1, 'Cafe': 8},
    'Office': {'Cafe': 7, 'Hospital': 4}
}

start = 'Home'
goal = 'Theater'
shortest_path, distance = dijkstra_shortest_path(city_map, start, goal)
print("Кратчайший путь от Home до Theater:", shortest_path)
print("Общая длина пути:", distance)