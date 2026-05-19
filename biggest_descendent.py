def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    if biggest is None:
        biggest = {}
        
    max_val = value[root]
    
    for neighbor in graph.neighbors(root):
        biggest_descendent(graph, neighbor, value, biggest)
        max_val = max(max_val, biggest[neighbor])
        
    biggest[root] = max_val
    
    return biggest