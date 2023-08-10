from solutions import valid_parentheses


class TestCases:
    def test_valid_inputs(self, parentheses_inputs):
        assert valid_parentheses(parentheses_inputs[0][0]) == parentheses_inputs[0][1]
        assert valid_parentheses(parentheses_inputs[1][0]) == parentheses_inputs[1][1]

    def test_invalid_inputs(self, parentheses_inputs):
        assert valid_parentheses(parentheses_inputs[2][0]) == parentheses_inputs[2][1]
        assert valid_parentheses(parentheses_inputs[3][0]) == parentheses_inputs[3][1]
