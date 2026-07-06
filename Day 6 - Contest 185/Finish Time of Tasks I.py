class Solution:
    def finishTime(n, edges, baseTime):
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        def dfs(node):

            # leaf node
            if not graph[node]:
                return baseTime[node]

            # non leaf node
            child_times = []
            for child in graph[node]:
                child_times.append(dfs(child))

            earliest = min(child_times)
            latest = max(child_times)

            ownDuration = (latest - earliest) + baseTime[node]
            return latest + ownDuration

        return dfs(0)