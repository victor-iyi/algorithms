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


class Node(object):

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    def __repr__(self):
        return 'Node(data={}, next_node={})'.format(self._data,
                                                    self._next_node)

    def __str__(self):
        return 'Node(data={})'.format(self._data)

    def display(self):
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
        self._data = value

    @next_node.setter
    def next(self, value):
        self._next_node = value


if __name__ == '__main__':
    n1 = Node('Monday')
    n2 = Node('Tueday', next_node=n1)
    n3 = Node('Wednesday', next_node=n2)

    n3.display()
