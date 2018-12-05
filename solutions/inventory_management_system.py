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
    if has_specific_count(box_id, specific_count):
        return 1
    return 0


def has_specific_count(box_id, count_in_question):
    counter = Counter(box_id)
    return any(count == count_in_question for _, count in counter.items())


if __name__ == "__main__":
    with open("inputs/inventory_management_system.yaml", "r") as box_ids:
        test_input = yaml.safe_load(box_ids)

    print("Part One:", calculate_checksum(test_input.split()))
