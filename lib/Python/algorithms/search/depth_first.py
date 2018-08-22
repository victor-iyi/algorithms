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


def dfs(graph, start, func=None, visited=None, **kwargs):
    """Depth first search/traversal.

    Implemented using Stacks to keep track of visted nodes.

    Arguments:
      graph {dict} -- Graph elements.
      start {any} -- Start node.

    Keyword Arguments:
      func {callable} -- Function to be performed on each node.
          (default: {print})
      visited {set} -- Keeping track of visited node. Stack data structure.
          (default: {None})

    Returns:
      [type] -- [description]
    """
    # Visited set to keep track of visited node.
    visited = visited or set()

    # Add node to visited set.
    visited.add(start)

    if callable(func):
        func(start, **kwargs)

    for node in graph[start] - visited:
        dfs(graph, node, func=func, visited=visited, **kwargs)

    return visited


if __name__ == '__main__':

    elements = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }

    # Depth first traversal.
    dfs(elements, 'a', func=print, end=' ')
