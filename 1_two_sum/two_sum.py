def two_sum(numbers, target):
    number_map = {}

    for i, number in enumerate(numbers):
        missing_number = target - number
        if missing_number in number_map:
            return [number_map[missing_number], i]
        number_map[number] = i

    return []
