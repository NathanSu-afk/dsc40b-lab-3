import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    target_index = k - 1

    def select(left, right):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        pivot_distance = abs(arr[right] - q)
        fill_pointer = left

        for i in range(left, right):
            if abs(arr[i] - q) < pivot_distance:
                arr[fill_pointer], arr[i] = arr[i], arr[fill_pointer]
                fill_pointer += 1

        arr[fill_pointer], arr[right] = arr[right], arr[fill_pointer]

        if fill_pointer == target_index:
            return arr[fill_pointer]
        elif fill_pointer > target_index:
            return select(left, fill_pointer - 1)
        else:
            return select(fill_pointer + 1, right)

    kth_point = select(0, len(arr) - 1)
    distance = abs(kth_point - q)
    return (distance, kth_point)