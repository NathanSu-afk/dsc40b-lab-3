def swap_sum(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    numerator = sum_A - sum_B + 10
    if numerator%2 != 0:
        return None
    target = numerator//2
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        diff = A[i] - B[j]
        if diff == target:
            return (i, j)
        elif diff < target:
            i += 1
        else:
            j += 1
    return None