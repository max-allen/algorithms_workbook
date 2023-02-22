# BST Construction

# Implement the insert, contains, and remove BST methods.

# Note the following:

# Remove method should only operate on the first instance.

# Values cant be removed from a single node tree, so calling
# remove on a single node should do nothing.

# Each BST node should have an integer value. It can have left
# and right child nodes. Child nodes must be valid BST nodes;
# they should possess the values None or Null if empty.

class BSTConstruction:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        return self

    def contains(self, value):
        pass

    def remove(self, value):
        return self
