import random


def interval_binary_search(arr, value):
    iterations_count = 0

    if len(arr) == 0:
        return (iterations_count, None)

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        iterations_count += 1
        mid = (high + low) // 2
        current = arr[mid] - value

        if mid - 1 >= 0:
            previous = arr[mid - 1] - value
        if current >= 0 and previous < 0:
            if abs(previous) < abs(current):
                mid = mid - 1
            break

        if mid + 1 < len(arr):
            next = arr[mid + 1] - value
        if current <= 0 and next > 0:
            if abs(next) < abs(current):
                mid = mid + 1
            break

        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1

    return (iterations_count, arr[mid])


if __name__ == "__main__":
    bound = 20
    arr = sorted([random.uniform(0, bound) for _ in range(bound)])
    print("Array:")
    print(arr)
    print()

    test_values = (random.uniform(0, bound // 4), random.uniform(bound // 5 * 2,  bound // 5 * 3),
                   random.uniform(bound // 4 * 3, bound), arr[random.randint(0, bound)], 0, bound)
    test_types = ["lower part", "mid part",
                  "upper part", "random from array", "min", "max"]

    for value, test_type in zip(test_values, test_types):
        iterations, el = interval_binary_search(arr, value)
        print(f"Result of interval binary search for element {
              value} ({test_type}):")
        print("Iterations:", iterations)
        print("Closest element:", el)
        print()
