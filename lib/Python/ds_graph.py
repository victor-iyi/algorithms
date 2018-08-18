"""Graph data structure

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds_graph.py
     Created on 18 August, 2018 @ 12:27 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class Graph(object):
    """Graph is a pictorial representation of set of objects where
    some pairs of objects are connected by links. The interconnected
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
        self.g = g or {}
        self.v = self.e = set()

    def __repr__(self):
        return 'Graph()'

    @classmethod
    def from_dict(cls, d):
        inst = cls(d)
        return inst


if __name__ == '__main__':
    pass
