import unittest

from solutions.chronal_calibration import adjust_frequency, cycle_for_repeat


class ChronalCalibrationTests(unittest.TestCase):
    def test_sums_inputs_to_final_drift(self):
        result = adjust_frequency(["+1", "+1", "+1"])
        self.assertEqual(result, 3)

    def test_adjusts_negatively(self):
        result = adjust_frequency(['-1', '-2', '-3'])
        self.assertEqual(result, -6)

    def test_adjusts_both_as_needed(self):
        result = adjust_frequency(["+1", "-2", "+3", "+1"])
        self.assertEqual(result, 3)

    def test_cycles_through_modulations_till_it_hits_a_repeat(self):
        result = cycle_for_repeat(["+3", "+3", "+4", "-2", "-4"])
        self.assertEqual(result, 10)

    def test_another_example(self):
        result = cycle_for_repeat(["-6", "+3", "+8", "+5", "-6"])
        self.assertEqual(result, 5)

    def test_one_more_example(self):
        result = cycle_for_repeat(["+7", "+7", "-2", "-7", "-4"])
        self.assertEqual(result, 14)
