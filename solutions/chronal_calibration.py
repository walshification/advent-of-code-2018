import itertools

import yaml


def adjust_frequency(modulations):
    return sum(int(modulation) for modulation in modulations)


def cycle_for_repeat(modulations):
    frequencies = [0]
    total = 0
    for modulation in itertools.cycle(modulations):
        delta = int(modulation)
        total += delta
        if total in frequencies:
            return total
        else:
            frequencies.append(total)


if __name__ == "__main__":
    with open("inputs/chronal_calibration.yaml", "r") as modulations:
        test_input = yaml.safe_load(modulations)

    print("Part One:", adjust_frequency(test_input.split()))
    print("Part Two:", cycle_for_repeat(test_input.split()))
