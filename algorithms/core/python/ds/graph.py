"""Data Structure: Graphs.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/graph.py
     Created on 22 August, 2018 @ 9:01 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""

from typing import Dict, List


class Graph(object):
    """Graph is a pictorial representation of set of objects.

    Some pairs of objects are connected by links. The interconnected
    objects are represented by points termed as vertices and the links
    that connect the vertices are called Edges.

    Operations:
        - Create a graph.
        - Display graph vertices
        - Display graph edges
        - Add a vertex
        - Add an edge
    """

    def __init__(self, g=None):
        self.g = g or dict()
        self.v = self.e = set()

    def __repr__(self):
        return 'Graph()'

    def __getitem__(self, item):
        return self.g[item]

    @classmethod
    def from_dict(cls, d: Dict[str, List[str]]):
        """Create a graph object from a dictionary of vertices and edges.

        Dictionary takes the form of:
            elements = {
              'a': [ 'b', 'c' ],
              'b': [ 'a', 'd' ],
              'c': [ 'a', 'd' ],
              'd': [ 'e' ],
              'e': [ 'd' ],
            }

        Arguments:
          d: {dict} -- A dictionary containing vertices and edges.

        Returns:
          Graph -- An initialized Graph object.
        """
        inst = cls(d)
        return inst

    def addEdge(self, e):
        pass

    def addVertex(self, v):
        pass

    def display(self):
        pass

    @property
    def edges(self):
        return []

    @property
    def vertices(self):
        return list(self.g.keys())


if __name__ == '__main__':
    elements = {
        'a': set([]),
    }

    graph = Graph()
    graph.display()
