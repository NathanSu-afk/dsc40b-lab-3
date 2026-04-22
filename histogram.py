def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both "points" and "bins" are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    k = len(bins)
    counts = [0]*k
    bin_idx = 0
    
    for point in points:
        while bin_idx < k and point >= bins[bin_idx][1]:
            bin_idx += 1
        if bin_idx < k:
            counts[bin_idx] += 1
            
    densities = []
    for i in range(k):
        current_bin = bins[i]
        a = current_bin[0]
        b = current_bin[1]
        width = b-a
        density = counts[i]/(n*width)
        densities.append(density)
        
    return densities