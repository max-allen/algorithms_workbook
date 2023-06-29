from solutions import get_nth_fibonacci


class TestCases:
    def test_return_values(self, get_nth_fibonacci_sequence):
        """Should correctly return nth element in sequence"""
        expected = [
            get_nth_fibonacci_sequence[4],
            get_nth_fibonacci_sequence[10],
            get_nth_fibonacci_sequence[6],
        ]

        result = [
            get_nth_fibonacci(5),
            get_nth_fibonacci(11),
            get_nth_fibonacci(7),
        ]

        assert expected == result
