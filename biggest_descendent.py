def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    if biggest is None:
        biggest = {}
        
    def solve(node):
        max_val = value[node]
        for neighbor in graph.neighbors(node):
            max_val = max(max_val, solve(neighbor))
        biggest[node] = max_val
        return max_val

    solve(root)
    
    return None