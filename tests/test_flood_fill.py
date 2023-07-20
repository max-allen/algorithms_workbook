from solutions import flood_fill


class TestCases:
    def test_color_change(self, flood_fill_color_change):
        assert (
            flood_fill(
                flood_fill_color_change["input"],
                flood_fill_color_change["start_row"],
                flood_fill_color_change["start_col"],
                flood_fill_color_change["color"],
            )
            == flood_fill_color_change["expected"]
        )

    def test_no_connection(self, flood_fill_no_connection):
        assert (
            flood_fill(
                flood_fill_no_connection["input"],
                flood_fill_no_connection["start_row"],
                flood_fill_no_connection["start_col"],
                flood_fill_no_connection["color"],
            )
            == flood_fill_no_connection["expected"]
        )
