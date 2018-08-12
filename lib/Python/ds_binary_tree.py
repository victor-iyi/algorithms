class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left, self.right = None

    def insert(self, value):
        if value <= self.data:
            # Insert to the left node.
            if self.left is None:
                self.left = value
            else:
                self.insert(value)
        else:
            # Insert tot the right node.
            if self.right is None:
                self.right = value
            else:
                self.insert(value)

    def contains(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left is None:
                return False
            else:
                return self.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.contains(value)
