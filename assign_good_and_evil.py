def assign_good_and_evil(graph):
    labels = {}
    
    for start_node in graph.nodes:
        if start_node not in labels:
            # Start a traversal (e.g., using a queue for BFS)
            labels[start_node] = 'good'
            stack = [start_node]
            
            while stack:
                u = stack.pop()
                for v in graph.neighbors(u):
                    if v not in labels:
                        # Assign opposite label
                        labels[v] = 'evil' if labels[u] == 'good' else 'good'
                        stack.append(v)
                    elif labels[v] == labels[u]:
                        # Conflict found: rivalry between same labels
                        return None
    return labels