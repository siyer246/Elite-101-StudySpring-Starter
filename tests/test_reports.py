import unittest
from features import reports

class TestCase(unittest.TestCase):

    def test_empty_history(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)

    def test_several_score(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)

    if __name__ == "__main__":
        unittest.main()