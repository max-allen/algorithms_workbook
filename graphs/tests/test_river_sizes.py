from graphs import river_sizes


class TestCases:
    def test_sizes(self, river_sizes_matrix):
        assert (
            river_sizes(river_sizes_matrix["matrix"]) == river_sizes_matrix["expected"]
        )
