def  has_cycle(graph):
    visiting = set()
    visited = set()
    
    for node in graph:
        if cycle_detect(graph, node, visiting, visited):
            return True
    return False

def cycle_detect(graph, node, visiting, visited):
    if node in visiting:
        return True
    if node in visited:
        return False
    
    visiting.add(node)
    
    for neighbor in graph.get(node,[]):
        if cycle_detect(graph, neighbor, visiting, visited):
            return True
    
    visiting.remove(node)
    visited.add(node)
    
    return False


print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True
    
    