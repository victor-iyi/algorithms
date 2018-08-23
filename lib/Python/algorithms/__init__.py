"""Algorithms like Search and sort algorithms, including BFS, DFS, BST etc.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: __init__.py
     Created on 22 August, 2018 @ 8:54 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

from algorithms.search.depth_first import DFS
from algorithms.search.breadth_first import BFS

# from algorithms.sort.merge import merge
# from algorithms.sort.bubble import bubble


__all__ = [
    # Search Algorithms.
    'BFS', 'DFS',

    # Sort Algorithms.
    # 'merge', 'bubble',
]
