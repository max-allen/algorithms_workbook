class TestCases:
    def test_depth_first_search(self, graph):
        g = graph["fixture"]
        assert g.depth_first_search("A") == graph["dfs_a_expected"]

    def test_breadth_first_search(self, graph):
        g = graph["fixture"]
        assert g.breadth_first_search("A") == graph["bfs_a_expected"]
