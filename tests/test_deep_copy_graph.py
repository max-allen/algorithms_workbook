from solutions import deep_copy, test_deep_copy as copy_test_helper


class TestCases:
    def test_copy_result(self, graph_nodes):
        orig = graph_nodes["n3"]
        copy = deep_copy(orig)
        result = copy_test_helper(orig, copy)
        assert result is True
