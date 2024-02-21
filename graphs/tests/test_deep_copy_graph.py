from graphs import deep_copy


class TestCases:
    def test_copy_result(self, graph_nodes):
        orig = graph_nodes["n3"]
        copy = deep_copy(orig)

        def eval_copy(initial, copied):
            assert initial != copied
            assert copied.value == initial.value
            assert len(copied.neighbors) == len(initial.neighbors)

            for idx, _ in enumerate(initial.neighbors):
                initial_neighbor, copied_neighbor = (
                    initial.neighbors[idx],
                    copied.neighbors[idx],
                )

                eval_copy(initial_neighbor, copied_neighbor)

        eval_copy(orig, copy)
