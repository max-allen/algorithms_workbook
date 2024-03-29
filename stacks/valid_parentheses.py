# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:


# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# "((({{{}}})))" -> True


def valid_parentheses(s):
    stack = []
    char_hash = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in char_hash:
            stack.append(char_hash[char])
        else:
            closing_char = stack.pop() if stack else None
            if char != closing_char:
                return False

    return not stack
