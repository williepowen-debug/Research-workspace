"""L546: a Leg-B share exactly ON the bar must grade SPENT (letter: <= 4.909%), never by float luck."""
import importlib.util
from pathlib import Path
from unittest.mock import patch
import unittest

spec = importlib.util.spec_from_file_location('cot', Path(__file__).resolve().parents[1] / 'cot_grade.py')
cot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cot)


class LegBEdge(unittest.TestCase):
    def test_exact_edge_at_frozen_bar_is_spent(self):
        self.assertEqual(cot.leg_b(4909, 100000), 'SPENT')
        self.assertEqual(cot.leg_b(4909 * 7, 100000 * 7), 'SPENT')

    def test_one_contract_over_is_not_spent(self):
        self.assertEqual(cot.leg_b(4910, 100000), 'NOT-SPENT')

    def test_exact_edge_where_float_misgrades(self):
        # 4007/100000*100 == 4.007000000000001 in float: the old compare said NOT-SPENT.
        self.assertFalse(4007 / 100000 * 100.0 <= 4.007)
        with patch.object(cot, 'LEG_B_BAR_PCT', 4.007):
            self.assertEqual(cot.leg_b(4007, 100000), 'SPENT')
            self.assertEqual(cot.leg_b(4008, 100000), 'NOT-SPENT')

    def test_recorded_vintages_unchanged(self):
        # 9/22 #7 and 9/29 #8 from STATUS ladder: both NOT-SPENT.
        self.assertEqual(cot.leg_b(121362, 1841811), 'NOT-SPENT')
        self.assertEqual(cot.leg_b(129436, 1878576), 'NOT-SPENT')


if __name__ == '__main__':
    unittest.main()
