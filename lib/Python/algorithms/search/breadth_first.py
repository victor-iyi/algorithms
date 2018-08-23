"""Search Algorithms: Breadth First Search.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: search/breadth_first.py
     Created on 22 August, 2018 @ 9:02 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

from collections import deque


class BFS:

    @staticmethod
    def recursive(graph, start, visited=None, queue=None):
        """Recursive solution to Breadth first serach.

        Breadth First Traversal uses Queue to keep track of visited
        nodes. The `collections.deque` was used to mimic a queue here.

        Arguments:
          graph {dict} -- Graph elements.
          start {any} -- Start node.

        Keyword Arguments:
          visited {set} -- List of visited nodes. (default: {None})
          queue {deque} -- List of unvisted nodes. (default: {None})

        Returns:
          set -- Visited nodes.
        """
        visited = visited or set([start])
        queue = queue or deque([start])

        # Extend the first element in the visited queue.
        vertex = queue.popleft()
        BFS.display(vertex, end=' ')

        # Go through it's children.
        for node in graph[vertex]:
            if node not in visited:
                # Visit this node.
                queue.append(node)

                # Mark as visited
                visited.add(node)

                # Recursively visit nodes.
                BFS.recursive(graph, node, visited=visited, queue=queue)

        return visited

    @staticmethod
    def iterative(graph, start):
        """Iterative solution to Breadth First Search.

        Breath first traversal uses Queues to keep track of unvisited nodes.
        Here, `collections.deque` was used to mimic a Python Queue.

        Arguments:
          graph {dict} -- Graph data elements.
          start {any} -- Start node.

        Returns:
          set -- Visited nodes.
        """
        visited = set([start])     # Visited nodes.
        queue = deque([start])  # Unvisited nodes.

        while queue:
                # Get the first element from the queue.
            vertex = queue.popleft()
            BFS.display(vertex, end=' ')

            # Extend it's children
            for node in graph[vertex]:
                    # If it's children isn't visited
                if node not in visited:
                    # Add it to the end of the queue.
                    queue.append(node)

                    # Mark node as visited.
                    visited.add(node)

        return visited

    @staticmethod
    def display(*args, **kwargs):
        """Display method for Breadth first search.

        See `help(print)` for more details.

        Arguments:
          *args {list} -- Argument list.
          **kwargs {dict} -- List of Keyword arguments.
        """
        print(*args, **kwargs)


if __name__ == '__main__':

    elements = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["E"],
        "E": ["A"],
    }

    print('Recursive Solution:')
    BFS.recursive(elements, 'A')
    print('\n')

    print('Iterative Solution:')
    BFS.iterative(elements, 'A')
    print('\n')
