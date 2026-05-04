def mode(numbers):
    if not numbers:
        return None
    
    counts = {}
    best_mode = numbers[0]
    max_frequency = 0
    
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
        
        if counts[num] > max_frequency:
            max_frequency = counts[num]
            best_mode = num
            
    return best_mode