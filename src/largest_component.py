def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size
    return largest
        
def explore_size(graph, node, visited):
    size = 1
    if node in visited:
        return 0
    visited.add(node)
    for neighbor in graph[node]:
        size += explore_size(graph,neighbor, visited)
    return size
    
    
    
    
    

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4