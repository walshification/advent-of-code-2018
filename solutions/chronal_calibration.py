import yaml


def adjust_frequency(modulations):
    return sum(int(modulation) for modulation in modulations)


if __name__ == "__main__":
    with open('inputs/chronal_calibration.yaml', 'r') as modulations:
        test_input = yaml.safe_load(modulations)
    adjusted = adjust_frequency(test_input.split())
    print('Part One:', adjusted)
