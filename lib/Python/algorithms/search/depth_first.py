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

    # Goal node.
    goal = 'G'

    @staticmethod
    def recursive(graph, start, visited=None, toVisit=None):
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
        visited = visited or [start]
        toVisit = toVisit or [start]

        vertex = toVisit.pop()
        if DFS.func(vertex):
            return True

        for child in graph[vertex]:
            if child not in visited:
                visited.append(child)
                toVisit.append(child)

                # Recursively visit child nodes.
                return DFS.recursive(graph, child, visited=visited,
                                     toVisit=toVisit)

        return False

    @staticmethod
    def iterative(graph, start):
        visited = [start]
        toVisit = [start]     # Stack DS.

        while toVisit:
            # Take from the end of visited.
            vertex = toVisit.pop()

            if DFS.func(vertex):
                return True

            for child in graph[vertex]:
                if child not in visited:
                    visited.append(child)
                    toVisit.append(child)

        return False

    @staticmethod
    def func(vertex):

        print(vertex, end=' ')

        if vertex == DFS.goal:
            print('\nFound "{}"!'.format(DFS.goal))
            return True

        return False


if __name__ == '__main__':

    """
    GRAPH
    –––––

    A ----- B
    |       |
    |       |
    C ----- D --- E
    """
    graph1 = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["E"],
        "E": ["D"],
    }

    # Set the Goal to 'E'.
    DFS.goal = 'E'

    # Depth first traversal.
    print('Recursive solution:')
    DFS.recursive(graph1, 'A')
    print('\n')

    print('Iterative Solution:')
    DFS.iterative(graph1, 'A')
    print('\n')

    """
    GRAPH
    ––––––

        C --------- E
        |
        A
      / |           G
     /  |          /
    S --B -- D --/

    """
    graph2 = {
        'S': ['A', 'B'],
        'A': ['S', 'B', 'C'],
        'B': ['S', 'A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'G'],
        'E': ['C'],
        'G': ['D'],
    }

    # Set the Goal to 'G'
    DFS.goal = 'G'

    # Depth first traversal.
    print('Recursive solution:')
    DFS.recursive(graph2, 'S')
    print('\n')

    print('Iterative Solution:')
    DFS.iterative(graph2, 'S')
    print('\n')
