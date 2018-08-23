"""Depth First Search Algorithm implmentation.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: search/depth_first.py
     Created on 22 August, 2018 @ 8:57 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class DFS:

    @staticmethod
    def recursive(graph, start, visited=None):
        """Depth first search/traversal.

        Implemented using Stacks to keep track of visted nodes.

        Arguments:
          graph {dict} -- Graph elements.
          start {any} -- Start node.

        Keyword Arguments:
          visited {set} -- Keeping track of visited node. Stack data structure.
              (default: {None})

        Returns:
          set -- Vistited nodes.
        """
        # Visited set to keep track of visited node.
        visited = visited or set()

        # Add node to visited set.
        visited.add(start)

        DFS.display(start, end=' ')

        for node in graph[start] - visited:
            DFS.recursive(graph, node, visited=visited)

        return visited

    @staticmethod
    def iterative():
        pass

    @staticmethod
    def display(*args, **kwargs):
        print(*args, **kwargs)
        # pass


if __name__ == '__main__':

    elements = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }

    # Depth first traversal.
    print('Recursive solution:')
    DFS.recursive(elements, 'a')
    print('\n')
