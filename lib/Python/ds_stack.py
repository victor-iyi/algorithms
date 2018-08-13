"""In the English dictionary the word "Stack" means *arranging objects on over another*. It is the same way memory is
allocated in this data structure. It stores the data elements in a similar fashion as a bunch of plates are stored
one above another in the kitchen. So **Stack Data Structure** allows operations at one end which can be called top of
the stack. We can add elements or remove elements only form this end of the Stack.

Operations:
    - Create
    - pop/remove
    - push/add
    - peek - Check the first element in the stack.
    - Add elements to the top of a stack.
    - Remove last element from the stack.

Complexity:
    - Push  O(1)
    - Pop   O(1)
"""


class Stack(object):

    def __init__(self):
        self.stack = []

    def __repr__(self):
        return 'Stack({})'.format(', '.join(self.stack))

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[0]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) < 1:
            return None

        # Get the last element before deleting.
        last = self.stack[-1]

        # Remove the last element.
        del self.stack[-1]

        return last

    def add(self, value):
        # Ensure no duplicates.
        if value not in self.stack:
            self.push(value)
            return True

        # Value already in stack.
        return False

    def remove(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.pop()

    @classmethod
    def fromlist(cls, l):
        # Initialize the object.
        inst = cls()

        # Add all list element to the stack.
        for item in l:
            inst.push(item)

        return inst


if __name__ == '__main__':
    # Create an empty stack then push items to the stack.
    s = Stack()
    print('Starting size: {}'.format(len(s)))
    s.push("Monday")
    s.push("Tuesday")
    s.push("Wednesday")
    print('After pushing: {}'.format(len(s)))
    print(s.pop())
    print('After one `pop`: {}'.format(len(s)))

    # Create a Stack data structure from a list.
    s2 = Stack.fromlist([1, 2, 3, 4, 5, 6])
    print('\nSize of `s2`: {}'.format(len(s2)))
    print(s2.pop(), s2.pop(), s2.pop())
    print(s2.pop(), s2.pop(), s2.pop())
    print('Size of `s2`: {}'.format(len(s2)))
