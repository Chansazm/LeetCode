from collections import deque
class Solution:
    def has_path(self, edges, src, dst):
        queue = deque([src])
        visited = set()
                
        while queue:
            current = queue.popleft()
            if current == dst:
                return True
            if current in visited:
                continue
            visited.add(current)
            
            for neighbor in edges[current]:
                queue.append(neighbor)
        return False
    

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(Solution().has_path(graph, 'f', 'k'))


            
        
    