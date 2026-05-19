def cluster(graph, weights, level):
    '''
    Clusters a graph based on similarity.
    '''
    visited = set()
    all_clusters = []

    for node in graph.nodes:
        if node not in visited:
            current_cluster = []
            queue = [node]
            visited.add(node)
            
            while queue:
                curr = queue.pop(0)
                current_cluster.append(curr)
                
                for neighbor in graph.neighbors(curr):
                    if neighbor not in visited:
                        if weights(curr, neighbor) >= level:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
            all_clusters.append(frozenset(current_cluster))

    return frozenset(all_clusters)