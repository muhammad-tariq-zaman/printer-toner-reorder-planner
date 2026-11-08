import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import plan

def row(p, toner, ppd):
    return {"printer": p, "toner_percent": str(toner), "pages_per_day": str(ppd)}

class TestTonerPlanner(unittest.TestCase):
    def test_reorder(self):
        self.assertEqual(plan([row("HP-1", 10, 50)])[0][4], "REORDER")
    def test_ok(self):
        self.assertEqual(plan([row("HP-1", 80, 50)])[0][4], "OK")
    def test_days_calculation(self):
        days = plan([row("HP-1", 50, 50)])[0][3]
        self.assertAlmostEqual(days, 20.0)
    def test_zero_usage_unknown(self):
        self.assertEqual(plan([row("HP-1", 50, 0)])[0][4], "UNKNOWN")
    def test_soonest_empty_first(self):
        r = plan([row("A", 80, 50), row("B", 10, 50)])
        self.assertEqual(r[0][0], "B")
