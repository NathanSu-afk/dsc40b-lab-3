from dsc40graph import UndirectedGraph

def slc(graph, d, k):
    nodes = list(graph.nodes)
    num_nodes = len(nodes)
    
    if k >= num_nodes:
        return frozenset(frozenset([n]) for n in nodes)
    
    dsf = DisjointSetForest(nodes)
    sorted_edges = sorted(graph.edges, key=d)
    
    num_clusters = num_nodes
    
    for u, v in sorted_edges:
        if num_clusters <= k:
            break
            
        if not dsf.in_same_set(u, v):
            dsf.union(u, v)
            num_clusters -= 1

    clusters = {}
    for node in nodes:
        representative = dsf.find_set(node)
        if representative not in clusters:
            clusters[representative] = []
        clusters[representative].append(node)
        
    return frozenset(frozenset(cluster) for cluster in clusters.values())