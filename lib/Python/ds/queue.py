"""Data structures and algorithms.

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

    def __init__(self, q=None):
        self._queue = list(q) or []
        self._idx = 0

    def __repr__(self):
        q = ", ".join(map(str, self.queue))
        return 'Queue(q=[{}])'.format(q)

    def __contains__(self, value):
        return value in self._queue

    def __next__(self):
        if self._idx >= len(self._queue):
            self._idx = 0
            raise StopIteration()

        idx = self._idx
        self._idx += 1
        return self._queue[idx]

    def __iter__(self):
        for q in self._queue:
            yield q

    def __getitem__(self, item):
        # Indexing Queue.
        return self._queue[item]

    def __len__(self):
        # Get length of the queue
        return len(self._queue)

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


if __name__ == '__main__':
    q = Queue([1, 2, 3, 4, 5])
    print(q)

    q.add(6)
    print(q)

    print(q.remove(5))
    print(q)
