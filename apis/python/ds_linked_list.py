"""A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked list in its standard library. We implement the concept of linked lists using the concepts of nodes.

Singly Linked Lists:
    In this type of data structure there's only one link between any two data elements. We create such a list and create additional methods to insert, update and remove elements fromt the list.

Operations:
    - Create
    - Traverse
    - Insertion in a linked list.
        - Insert at the beginning of a linked list.
        - Insert at the end of linked list.
    - Remove an item from a linked list.
"""

"""Creating a Linked List.

A linked list is created by using the node class. We create a Node object and create another class to use this node object. We pass the appropriate values through the node object to point it to the next data elements.
"""

# pylint: disable=unused-variable


class Node:
    """Creation of a node.

    Keyword Arguments:
        dataval {str} -- Value to be stored in this node. (default: {None})
    """

    def __init__(self, dataval: str=None):
        self.dataval = dataval
        self.nextval = None

    def __repr__(self):
        return 'Node(dataval={})'.format(self.dataval)

    __str__ = __repr__


class SLinkedList:
    """Singly linked list where there's only one link between any two data elements."""

    def __init__(self):
        self.headval: Node = None

    def __repr__(self):
        return 'SLinkedList({})'.format(self.headval)

    __str__ = __repr__

    def traverse(self, func, *args, **kwargs):
        currval = self.headval

        # Continue operation until there's no more Node element.
        while currval is not None:
            # Call function to be performed
            func(currval, *args, **kwargs)

            # Assign the pointer of the next node element to the current data element.
            currval = currval.nextval


# Creation of linked list.
print('\nCreation of linked list')
slist = SLinkedList()
slist.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

# Link first node to second node.
slist.headval.nextval = e2

# Link second Node to thrid node.
e2.nextval = e3

print('slist.headval = {}'.format(slist.headval))
print('e2.nextval = {}'.format(e2.nextval))
print('e3.nextval = {}'.format(e3.nextval))


"""Traversing a LinkedList.

Singly Linked Lists can be traversed in only forward direction starting from the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element.
"""


def print_elements(val):
    print('currval = {}'.format(val))


print('\nTraversing a linked list.')
slist.traverse(print_elements)
