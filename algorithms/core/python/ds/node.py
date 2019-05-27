"""Data Structures: Node.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/node.py
     Created on 22 August, 2018 @ 8:57 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Normal Node.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class Node(object):
    """Node Data Structure.

    [description]
    """

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    def __repr__(self):
        return 'Node(data={}, next_node={})'.format(self._data,
                                                    self._next_node)

    def __str__(self):
        return 'Node(data={})'.format(self._data)

    def display(self):
        """Display current node and all it's connected nodes.

        Example:
            ```python
            >>> n1 = Node("Wed")
            >>> n2 = Node("Tue", next_node=n1)
            >>> n3 = Node("Wed", next_node=n2)
            >>> n3.display()
            Node(data=Mon) -> Node(data=Tue) -> Node(data=Wed) -> END
            ```
        """
        current = self
        while current is not None:
            print(current, end=' -> ')
            current = current.next_node

        print('END')

    @property
    def data(self):
        return self._data

    @property
    def next_node(self):
        return self._next_node

    @data.setter
    def data(self, value):
        """Setter for `Node.data`.

        Decorators:
            data.setter

        Arguments:
            value {any} -- Value of current node.
        """
        self._data = value

    @next_node.setter
    def next_node(self, value):
        """Setter for `Node.next_node`.

        Decorators:
            next_node.setter

        Arguments:
            value {Node} -- Next node of current node.
        """
        self._next_node = value


##############################################################################
# +——————————————————————————————————————————————————————————————————————————+
# | Tree Node.
# +——————————————————————————————————————————————————————————————————————————+
##############################################################################
class TreeNode(object):
    """A TreeNode commonly used in data structures such as Binary Search Trees.

    Methods:

        def __lt__(other):
            # self.data < other.data

        def __le__(other):
            # self.data <= other.data

        def __gt__(other):
            # self.data > other.data

        def __ge__(other):
            # self.data >= other.data

        def __eq__(other):
            # self.data == other.data

        def __ne__(other):
            # self.data != other.data

        def insert(value):
            Insert a new Node to the Tree.

        def contains(value):
            Check if `value` is in the tree.

        def traverse(kind):
            Walk through the node and performs some function.

    Parameters:
        data: Data element in current node.
        left: Left node of current node.
        right: Right node of current node.
    """

    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    def __lt__(self, other):
        # Less than.
        return self.data < other.data

    def __le__(self, other):
        # Less than or equal to.
        return self.data <= other.data

    def __gt__(self, other):
        # Greater than.
        return self.data > other.data

    def __ge__(self, other):
        # Greater than or equal to.
        return self.data >= other.data

    def __eq__(self, other):
        # Equal to.
        return self.data == other.data

    def __ne__(self, other):
        # Not equal to.
        return self.data != other.data

    def insert(self, node):
        """Insert a new Node to the Tree.

        Using Recursion to insert a new node to the appropriate
        position in the Tree.

        Arguments:
            value {any} -- Value of the tree to be inserted.
        """
        if node <= self.data:
            # Insert to the left node.
            if self.left is None:
                self.left = node
            else:
                self.insert(node)
        else:
            # Insert tot the right node.
            if self.right is None:
                self.right = node
            else:
                self.insert(node)

    def contains(self, value):
        """Check if `value` is in the tree.

        True if value is in the tree history, False otherwise.

        Arguments:
            value {any} -- Value to be checked.

        Returns:
            bool -- True if value is present in tree, False otherwise.
        """
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

    def traverse(self, kind='in', func=print, **kwargs):
        """Walk through the node and performs some function.

        Function can be anything you want to do at each step of the
        walkthrough.

        Keyword Arguments:
            kind {str} -- Kind of traversal. In-order, Pre-order or Post-order
                traversal (default: {'in'})

            func {callable} -- A callable to execute on each node.
                e.g lambda node, **kwargs: print(f'{node}', **kwargs)

        Raises:
            ValueError -- `kind` must be one of 'in', 'pre', 'post'.
        """
        kinds = ('in', 'pre', 'post')

        if kind not in kinds:
            raise ValueError(f'`kind` must be one of {"".join(kinds)}')

        if kind == 'in':
            # Left -> Root -> Right.
            # Left node.
            if self.left is not None:
                self.traverse(kind=kind)

            # Root Node.
            if callable(func):
                func(self.data, **kwargs)

            # Right node.
            if self.right is not None:
                self.traverse(kind=kind)

        elif kind == 'pre':
            # Root -> Left -> Right.
            # Root node.
            if callable(func):
                func(self.data, **kwargs)

            # Left node.
            if self.left is not None:
                self.traverse(kind=kind)

            # Right node.
            if self.right is not None:
                self.traverse(kind=kind)
        else:
            # Left -> Right -> Root.
            # Left node.
            if self.left is not None:
                self.traverse(kind=kind)

            # Right node.
            if self.right is not None:
                self.traverse(kind=kind)

            # Root node.
            if callable(func):
                func(self.data, **kwargs)


if __name__ == '__main__':
    n1 = Node('Monday')
    n2 = Node('Tueday', next_node=n1)
    n3 = Node('Wednesday', next_node=n2)

    n3.display()
