def learn_theta(data, colors):
    blue_points = [d for d, c in zip(data, colors) if c == 'blue']
    red_points = [d for d, c in zip(data, colors) if c == 'red']
    return (max(blue_points) + min(red_points)) / 2

def compute_ell(data, colors, theta):
    loss = 0
    for d, c in zip(data, colors):
        if c == 'red' and d <= theta:
            loss += 1
        elif c == 'blue' and d > theta:
            loss += 1
    return float(loss)

def minimize_ell(data, colors):
    candidates = sorted(data)
    best_theta = candidates[0]
    min_loss = compute_ell(data, colors, best_theta)
    for theta in candidates:
        current_loss = compute_ell(data, colors, theta)
        if current_loss < min_loss:
            min_loss = current_loss
            best_theta = theta
    return float(best_theta)

def minimize_ell_sorted(data, colors):
    combined = sorted(zip(data, colors))
    n = len(combined)
    blue_total = sum(1 for c in colors if c == 'blue')
    blue_gt_theta = blue_total
    red_le_theta = 0
    min_loss = blue_gt_theta + red_le_theta
    best_theta = combined[0][0] - 1
    for i in range(n):
        val, color = combined[i]
        if color == 'red':
            red_le_theta += 1
        else:
            blue_gt_theta -= 1
        current_loss = blue_gt_theta + red_le_theta
        if current_loss < min_loss:
            min_loss = current_loss
            best_theta = val
    return float(best_theta)