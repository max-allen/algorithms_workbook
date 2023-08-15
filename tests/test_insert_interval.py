from solutions import insert_interval


class TestCases:
    def test_result(self, sorted_intervals):
        assert (
            insert_interval(
                sorted_intervals[0]["existing_intervals"],
                sorted_intervals[0]["insert_interval"],
            )
        ) == sorted_intervals[0]["expected"]

        assert (
            insert_interval(
                sorted_intervals[1]["existing_intervals"],
                sorted_intervals[1]["insert_interval"],
            )
        ) == sorted_intervals[1]["expected"]
