import unittest

from solutions.inventory_management_system import (
    calculate_checksum,
    count_duple_scans,
    count_treble_scans,
)


class InventoryManagementSystemTests(unittest.TestCase):
    def test_count_duple_scans_returns_zero_if_scans_dont_have_letters_the_same(self):
        count = count_duple_scans(["asdf"])
        self.assertEqual(count, 0)

    def test_count_duple_scans_returns_one_if_scan_has_double_letters(self):
        count = count_duple_scans(["aasdf"])
        self.assertEqual(count, 1)

    def test_count_duple_scans_can_count_more_than_one_id(self):
        count = count_duple_scans(["aasdf", "cdbb"])
        self.assertEqual(count, 2)

    def test_count_treble_scans_returns_one_if_scan_has_triple_letters(self):
        count = count_treble_scans(["aaasdf"])
        self.assertEqual(count, 1)

    def test_count_treble_scans_can_count_more_than_one_id(self):
        count = count_treble_scans(["aaasdf", "cdbbb"])
        self.assertEqual(count, 2)

    def test_calculate_checksum_returns_product_of_scan_counts(self):
        box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        checksum = calculate_checksum(box_ids)
        self.assertEqual(checksum, 12)
