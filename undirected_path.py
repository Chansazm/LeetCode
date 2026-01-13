from collections import deque
class Solution:
    def undirected_path(self, edges, src, dst):
        graph = self.build_graph(edges)
        return self.has_path(graph, src, dst)
    
    def has_path(self,graph, node_A, node_B):
        seen = set()
        queue = deque([node_A])
        if node_A == node_B:
            return True
        
        while queue:
            current = queue.popleft()
            if current == node_B:
                return True
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                queue.append(neighbor)
        return False
        
    def build_graph(self, edges):
        graph = {}
            
        for arr in edges:
            a, b = arr
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
                
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(Solution().undirected_path(edges, 'j', 'm')) # -> True
            
        