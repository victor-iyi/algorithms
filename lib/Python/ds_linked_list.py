"""A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked list in its standard library. We implement the concept of linked lists using the concepts of nodes.

Singly Linked Lists:
    In this type of data structure there's only one link between any two data elements. We create such a list and create additional methods to insert, update and remove elements from the list.

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
        data {str} -- Value to be stored in this node. (default: {None})
    """

    def __init__(self, data: str=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(data={})'.format(self.data)

    __str__ = __repr__


class SLinkedList:
    """Singly linked list where there's only one link between any two data elements."""

    def __init__(self):
        self.head = None

    def __repr__(self):
        return 'SLinkedList({})'.format(self.head)

    __str__ = __repr__

    def traverse(self, func=None, *args, **kwargs):
        # Handle empty LinkedList.
        if self.head is None:
            return

        curr_val = self.head

        # Continue operation until there's no more Node element.
        while curr_val is not None:
            # Call function to be performed
            if func is not None:
                func(curr_val, *args, **kwargs)

            # Assign the pointer of the next node element to the current data element.
            curr_val = curr_val.next

    def insert(self, newdata, pos='start', node: Node=None):
        allowed = ['start', 'end', 'at']
        if pos in allowed:
            raise ValueError('pos must be one of {}'.format(','.join(allowed)))

        if pos == 'at' and type(node) != Node:
            raise TypeError('`node` must be supplied when `pos=at`.')

        newNode = Node(data=newdata)

        if pos == 'start':
            # Update the new node's next to the existing node.
            newNode.next = self.head
            self.head = newNode
        elif pos == 'end':
            if self.head is None:
                self.head = newNode
                return
            # Go all the way through the linked list.
            current = self.head
            while current.next is not None:
                current = current.next

            # Ad the newNode to the end of the list.
            current.next = newNode

        else:
            # Update the new node's next to the given node.
            newNode.next = node.next
            node.next = newNode


if __name__ == '__main__':
    # Creation of linked list.
    print('\nCreation of linked list')
    slist = SLinkedList()
    slist.head = Node("Mon")

    e2 = Node("Tue")
    e3 = Node("Wed")

    # Link first node to second node.
    slist.head.next = e2

    # Link second Node to third node.
    e2.next = e3

    print('slist.head = {}'.format(slist.head))
    print('e2.next = {}'.format(e2.next))
    print('e3.next = {}'.format(e3.next))


    """Traversing a LinkedList.

    Singly Linked Lists can be traversed in only forward direction starting from the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element.
    """

    print('\nTraversing a linked list.')
    slist.traverse(lambda val: print('{}'.format(val)))
