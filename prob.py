import itertools

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def tsp(cities):
    best_route = None
    shortest_distance = float('inf')

    for route in itertools.permutations(cities):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += calculate_distance(route[i], route[i+1])
        total_distance += calculate_distance(route[-1], route[0])  # Return to start

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            best_route = route

    return best_route, shortest_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 6), (5, 3), (3, 1)] # Example cities (x, y coordinates)
    best_route, shortest_distance = tsp(cities)

    print("Best Route:", best_route)
    print("Shortest Distance:", shortest_distance)