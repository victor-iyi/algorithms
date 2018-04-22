"""There are situations when the allocation of memory to store the data cannot be in a continuous block of memory. So we take help of pointers along with the data, the address of the next location of data element is also stored. So we know the address of the next data element from the values of current data element. In general such structures are knowns as Pointers, but in Python we refer to them as Nodes.

Nodes are foundations on which various other data structures linked lists and trees can be handled in Python. There are two major operations that can be performed on Nodes:
    - Create a Node.
    - Traverse the node elements.

Creation of Nodes:

    The nodes are created by implementing a class which will hold the pointers along with the data element. In the below example we create a class named DayNames to hold the names of weekdays. The `nextval` pointer is initialized to null and three nodes are initialized with values as shown. The `nextval` pointer of node `e1` points to `e3` while the `nextval` pointer of node `e3` points to `e2`.

        Example:
        ```python
        >>> class DayNames:
                def __init__(self, dataval=None):
                    self.dataval = dataval
                    self.nextval = None
        >>> e1 = DayNames('Mon')
        >>> e2 = DayNames('Tue')
        >>> e3 = DayNames('Wed')
        >>>
        >>> e1.nextval = e3  # e1 points to e3
        >>> e3.nextval = e2  # e3 points to e2
        ```

Traversing the Node Elements:
    
    We can traverse the elements of the node created above by creating a variable and assigning the first element to it. Then we use a while loop and `nextval` pointer to print out all the node elements. Note that we have one more additional data element and `nextval` pointers are properly arranged to get the output as a day of a week in a proper sequence.

    Example:
        ```python
        >>> class DayNames:
                def __init__(self, dataval=None):
                    self.dataval = dataval
                   self.nextval = None
        >>> e1 = DayNames('Mon') 
        >>> e2 = DayNames('Wed')
        >>> e3 = DayNames('Tue')
        >>> e4 = DayNames('Thu')
        >>>
        >>> e1.nextval = e3
        >>> e3.nextval = e2
        >>> e2.nextval = e4
        >>>
        >>> thisval = e1
        >>> while thisvalue:
                print(thisval.dataval)
                thisval = thisval.nextval
        Mon
        Tue
        Wed
        Thu

        ```

The additional operations like insertion and deletion can be done by implementing appropriate methods by using this node containers in the general data structures like linked lists and trees.
"""

class DayNames:
    """Creating a node called DayNames. DayNames has a data value which holds the
    values for a day, and also nextval which points to the next node value.
    """

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def __repr__(self):
        return 'DayNames(dataval="{}")'.format(self.dataval)

    def __str__(self):
        return 'DayNames(dataval="{}")'.format(self.dataval)


e1 = DayNames('Mon')
e2 = DayNames('Tue')
e3 = DayNames('Wed')

e1.nextval = e3
e3.nextval = e2

print('e1: {}'.format(e1))
print('e2: {}'.format(e2))
print('e3: {}'.format(e3))
