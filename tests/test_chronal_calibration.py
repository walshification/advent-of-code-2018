import unittest

from solutions.chronal_calibration import adjust_frequency


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
