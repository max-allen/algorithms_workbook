from recursion import build_directory_structure


class TestCases:
    def test_result(self, filesystem_paths):
        assert (
            build_directory_structure(filesystem_paths["string"])
            == filesystem_paths["hash"]
        )
