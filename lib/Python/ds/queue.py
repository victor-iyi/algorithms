"""Data structures: Queue

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/queue.py
     Created on 23 August, 2018 @ 1:08 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class Queue(object):

    def __init__(self, *q):
        self._queue = list(q)

    def __repr__(self):
        return 'Queue({})'.format(', '.join(map(str, self._queue)))

    def __contains__(self, value):
        return value in self._queue

    def __iter__(self):
        for q in self._queue:
            yield q

    def __getitem__(self, item):
        # Indexing Queue.
        return self._queue[item]

    def __len__(self):
        # Get length of the queue
        return len(self._queue)

    @classmethod
    def fromlist(cls, l):
        return cls(*l)

    def peek(self):
        # Returns the first element in the list.
        if self._queue:
            return self._queue[0]

        return None

    def add(self, value):
        # Adds new element to the Queue.
        self._queue.append(value)

    def remove(self, value):
        # Remove an item from queu.
        if value in self._queue:
            self._queue.remove(value)
            return True
        return False

    def poll(self):
        """Removes the first element from the Queue.

        Returns:
          any -- First element in the Queue.
        """
        try:
            value = self._queue[0]
            del self._queue[0]
        except IndexError:
            value = None

        return value

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, value):
        self._queue = value


class PriorityQueue(object):
    pass


class Dequeue(object):
    pass


if __name__ == '__main__':
    q1 = Queue(1, 2, 3, 4, 5)
    print('q1 =', q1)

    q1.add(6)
    print('\tq1.add(6)')
    print('q1 =', q1)

    print('\tq1.remove(5) =', q1.remove(5))
    print('q1 =', q1)

    print('\tq1.poll() =', q1.poll())
    print('q1 =', q1)

    print()

    q2 = Queue.fromlist([1, 2, 3, 4])
    print('q2.poll() =', q2.poll())
    print('q2 =', q2, '\n')
