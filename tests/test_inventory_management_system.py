import unittest

from solutions.inventory_management_system import (
    calculate_checksum,
    count_duple_scans,
    count_treble_scans,
    filter_ids,
    id_union,
)


class CalculateCheckSumsTests(unittest.TestCase):
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


class IdUnionTests(unittest.TestCase):
    def test_returns_an_empty_string_if_no_characters_match(self):
        match = id_union("asdf", "qwer")
        self.assertEqual(match, "")

    def test_returns_a_single_matching_letter_if_it_matches(self):
        match = id_union("a", "a")
        self.assertEqual(match, "a")

    def test_skips_characters_that_do_not_match(self):
        match = id_union("bb", "bd")
        self.assertEqual(match, "b")

    def test_matches_against_any_number_of_characters(self):
        match = id_union("fghij", "fguij")
        self.assertEqual(match, "fgij")

    def test_filter_returns_empty_tuple_if_box_ids_are_totally_different(self):
        matching_ids = filter_ids(["asdf", "qwer"])
        self.assertEqual(matching_ids, ())

    def test_filter_returns_box_ids_if_they_are_just_one_character_off_each_other(self):
        matching_ids = filter_ids(["asdf", "awdf"])
        self.assertEqual(matching_ids, ("asdf", "awdf"))

    def test_filter_compares_one_id_to_all_others(self):
        matching_ids = filter_ids(["asdf", "qwer", "awdf"])
        self.assertEqual(matching_ids, ("asdf", "awdf"))
