from arrays import remove_duplicates


class TestCases:
    def test_removes_duplicate(self, array_with_duplicate):
        arr, expected = array_with_duplicate["arr"], array_with_duplicate["expected"]
        assert remove_duplicates(arr) == expected

    def test_removes_all_duplicates(self, array_with_several_duplicates):
        arr, expected = (
            array_with_several_duplicates["arr"],
            array_with_several_duplicates["expected"],
        )
        assert remove_duplicates(arr) == expected
