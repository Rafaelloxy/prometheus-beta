import heapq
from typing import List, Dict, Optional, Tuple

def johnsons_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph.
                                                  Each key is a vertex, and its value is a list of 
                                                  (destination, weight) tuples.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: A dictionary of shortest paths where the outer key 
                                             is the source vertex, inner key is destination vertex, 
                                             and value is the shortest path distance.
                                             Returns None if a negative cycle is detected.
    """
    # Step 1: Add a new vertex connected to all other vertices with zero-weight edges
    vertices = list(graph.keys())
    new_vertex = max(vertices) + 1
    graph[new_vertex] = [(v, 0) for v in vertices]
    
    # Step 2: Run Bellman-Ford to compute vertex potentials
    def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Optional[Dict[int, int]]:
        distances = {v: float('inf') for v in graph}
        distances[source] = 0
        
        # Relax edges |V| - 1 times
        for _ in range(len(graph) - 1):
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        # Check for negative cycles
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    return None
        
        return distances
    
    # Compute vertex potentials
    h = bellman_ford(graph, new_vertex)
    if h is None:
        return None  # Negative cycle detected
    
    # Remove the temporary vertex
    del graph[new_vertex]
    
    # Step 3: Reweight edges
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, weight in graph[u]:
            # Reweight = original weight + h(u) - h(v)
            reweighted_weight = weight + h[u] - h[v]
            reweighted_graph[u].append((v, reweighted_weight))
    
    # Step 4: Run Dijkstra's for each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = {}
        
        # Dijkstra's algorithm with min-heap
        dist = {v: float('inf') for v in graph}
        dist[source] = 0
        pq = [(0, source)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # If we've found a longer path, skip
            if current_dist > dist[u]:
                continue
            
            # Check all neighbors
            for v, weight in reweighted_graph[u]:
                distance = current_dist + weight
                
                # If we've found a shorter path
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # Adjust distances back to original weights
        for v in dist:
            if dist[v] != float('inf'):
                shortest_paths[source][v] = dist[v] - h[source] + h[v]
    
    return shortest_paths