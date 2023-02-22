import pytest
# from .two_number_sum import two_number_sum
from .solutions.iterative import two_number_sum

class TestCases:
  def test_one(self):
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    result = two_number_sum(arr, target)
    assert result == [-1, 11] or result == [11, -1]

  def test_two(self):
    arr = [4]
    target = 5
    assert two_number_sum(arr, target) == []
