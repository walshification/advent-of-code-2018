from collections import Counter

import yaml


def calculate_checksum(box_ids):
    duple_count = count_duple_scans(box_ids)
    treble_count = count_treble_scans(box_ids)
    return duple_count * treble_count


def count_duple_scans(box_ids):
    return sum(count_scan(box_id, 2) for box_id in box_ids)


def count_treble_scans(box_ids):
    return sum(count_scan(box_id, 3) for box_id in box_ids)


def count_scan(box_id, specific_count):
    counter = Counter(box_id)
    if any(count == specific_count for _, count in counter.items()):
        return 1
    return 0


def filter_ids(box_ids):
    for index, box_id in enumerate(box_ids):
        for i in range(index+1, len(box_ids)):
            next_id = box_ids[i % len(box_ids)]
            if len(id_union(box_id, next_id)) == len(box_id) - 1:
                return (box_id, next_id)
    return ()


def id_union(first_id, second_id):
    matches = []
    for first_char, second_char in zip(first_id, second_id):
        if first_char == second_char:
            matches.append(first_char)
    return "".join(matches)


if __name__ == "__main__":
    with open("inputs/inventory_management_system.yaml", "r") as test_input:
        box_ids = yaml.safe_load(test_input).split()

    print("Part One:", calculate_checksum(box_ids))
    print("Part Two:", id_union(*filter_ids(box_ids)))
