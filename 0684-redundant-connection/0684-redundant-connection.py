class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = [[] for i in range(n+1)]
        
        def dfs(node, par):
            if visited[node]:
                return True
            
            visited[node] = True
            for child in adjList[node]:
                if child == par:
                    continue

                if dfs(child, node):
                    return True

            return False

        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
            visited = [False] * (n + 1)
            
            if(dfs(v1, -1)):
                return [v1, v2]

        