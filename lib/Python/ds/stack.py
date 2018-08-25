"""Data structures: Stack

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/stack.py
     Created on 25 August, 2018 @ 10:43 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class Stack(object):

    def __init__(self, *s):
        self._stack = s

    @property
    def stack(self):
        return self._stack


if __name__ == '__main__':
    s = Stack()
