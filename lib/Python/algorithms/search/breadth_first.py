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


class BFS:

    @staticmethod
    def recursive(graph, start, visited=None):

        return visited

    @staticmethod
    def iterative(graph, start):
        pass

    @staticmethod
    def display(*args, **kwargs):
        print(*args, **kwargs)


if __name__ == '__main__':

    elements = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }

    BFS.iterative(elements, 'a')
