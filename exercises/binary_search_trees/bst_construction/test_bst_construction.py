import pytest
from bst_construction import bst_construction

class TestCases:
    def test_one(self):
        values = [20, 11, 5, 3, 30, 29]
        tree = bst_construction(values)
