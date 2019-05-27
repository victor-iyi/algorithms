class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

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

    def traverse(self, kind='in'):
        kinds = ('in', 'pre', 'post')
        if kind not in kinds:
            raise ValueError('`kind` must be one of {}'.format(''.join(kinds)))

        if kind == 'in':
            # Left -> Root -> Right.
            if self.left is not None:
                self.traverse(kind)
            print(self.data, end=' ')
            if self.right is not None:
                self.traverse(kind)
        elif kind == 'pre':
            # Root -> Left -> Right.
            print(self.data, end=' ')
            if self.left is not None:
                self.traverse(kind)
            if self.right is not None:
                self.traverse(kind)
        else:
            # Left -> Right -> Root.
            if self.left is not None:
                self.traverse(kind)
            if self.right is not None:
                self.traverse(kind)
            print(self.data, end=' ')
