"""Data structures: Stack

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/stack.py
     Created on 25 August, 2018 @ 10:43 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class Stack(object):
    """Stack Data Structure is a Last In First Out (LIFO)

    Stack is a Last In First Out (LIFO) data structure.
    It is very useful in many cases where order is important.
    """

    def __init__(self, *s):
        self._store = list(s)

    def __repr__(self):
        return 'Stack({})'.format(self._store)

    def __len__(self):
        return len(self._store)

    def __contains__(self, item):
        return item in self._store

    def __iter__(self):
        for s in self._store:
            yield s

    @classmethod
    def fromlist(cls, l):
        """Create a new stack from an existing iterable.

        Iterable can be a list/tuple/set or any object that supports
        object destruction: `*list`, `*tuple`, etc...

        Arguments:
            l {iter} -- An iterable.

        Returns:
            Stack -- Instance of Stack class.
        """
        inst = cls(*l)
        return inst

    def push(self, data):
        """Add an item to the end of the stack.

        Arguments:
            data {any} -- Data to be added to the Stack.
        """
        self._store.append(data)

    def pop(self):
        """Remove last added item from the stack.

        A Last In First Out (LIFO) method of removing the last added
        element from the stack.

        Returns:
            any -- Last added element or `None` if stack is empty.
        """
        if self._store:
            return self._store.pop()

        return None

    @property
    def store(self):
        return self._store


if __name__ == '__main__':
    # Create an empty stack.
    s1 = Stack()
    s1.push('Abraham')
    s1.push('Belinda')
    print(s1)
    s1.pop()
    print('{}\n'.format(s1))

    # Create a Stack with some existing data.
    s2 = Stack('Abraham', 'Belinda', 'Collin')
    print('{}\n'.format(s2))

    # Create a stack from an initial list/tuple
    initial = ['Dave', 'Edger', 'Frey']
    s3 = Stack.fromlist(initial)
    print('{}\n'.format(s3))
