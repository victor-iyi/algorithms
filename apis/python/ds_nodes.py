"""There are situations when the allocation of memory to store the data cannot be in a continuous block of memory. So
we take help of pointers along with the data, the address of the next location of data element is also stored. So we
know the address of the next data element from the values of current data element. In general such structures are
known as Pointers, but in Python we refer to them as Nodes.

Nodes are foundations on which various other data structures linked lists and trees can be handled in Python. There
are two major operations that can be performed on Nodes: - Create a Node. - Traverse the node elements.

Creation of Nodes:

    The nodes are created by implementing a class which will hold the pointers along with the data element. In the
    below example we create a class named DayNames to hold the names of weekdays. The `next` pointer is
    initialized to null and three nodes are initialized with values as shown. The `next` pointer of node `e1`
    points to `e3` while the `next` pointer of node `e3` points to `e2`.

        Example:
        ```python
        >>> class DayNames:
                def __init__(self, data=None):
                    self.data = data
                    self.next = None
        >>> e1 = DayNames('Mon')
        >>> e2 = DayNames('Tue')
        >>> e3 = DayNames('Wed')
        >>>
        >>> e1.next = e3  # e1 points to e3
        >>> e3.next = e2  # e3 points to e2
        ```

Traversing the Node Elements:
    
    We can traverse the elements of the node created above by creating a variable and assigning the first element to
    it. Then we use a while loop and `next` pointer to print out all the node elements. Note that we have one more
    additional data element and `next` pointers are properly arranged to get the output as a day of a week in a
    proper sequence.

    Example:
        ```python
        >>> class DayNames:
                def __init__(self, data=None):
                    self.data = data
                   self.next = None
        >>> e1 = DayNames('Mon') 
        >>> e2 = DayNames('Wed')
        >>> e3 = DayNames('Tue')
        >>> e4 = DayNames('Thu')
        >>>
        >>> e1.next = e3
        >>> e3.next = e2
        >>> e2.next = e4
        >>>
        >>> cur_val = e1
        >>> while cur_val:
                print(cur_val.data)
                cur_val = cur_val.next
        Mon
        Tue
        Wed
        Thu

        ```

The additional operations like insertion and deletion can be done by implementing appropriate methods by using this
node containers in the general data structures like linked lists and trees. """


# pylint: disable=unused-variable


class DayNames:
    """Creating a node called DayNames. DayNames has a data value which holds the
    values for a day, and also next which points to the next node value.
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'DayNames(data="{}")'.format(self.data)

    def __str__(self):
        return 'DayNames(data="{}")'.format(self.data)


# Creation of Nodes.
print('\nCreation of Nodes:')

e1 = DayNames('Mon')
e2 = DayNames('Tue')
e3 = DayNames('Wed')

e1.next = e3
e3.next = e2

print('e1: {}'.format(e1))
print('e2: {}'.format(e2))
print('e3: {}'.format(e3))

# Traversing Node elements.
print('\nTraversing Node elements:')

e1 = DayNames('Mon')
e2 = DayNames('Wed')
e3 = DayNames('Tue')
e4 = DayNames('Thu')

e1.next = e3
e3.next = e2
e2.next = e4

# Set `cur_val` to `next` of current node till end of the chain is reached.
cur_val = e1
while cur_val:
    print(cur_val.data)
    cur_val = cur_val.next

print('\nDisplay `next` for each nodes:')
print('e1.next = {}'.format(e1.next))
print('e2.next = {}'.format(e2.next))
print('e3.next = {}'.format(e3.next))
print('e4.next = {}'.format(e4.next))
