"""Backtracking algorithm.

   @description
     Backtracking is a form of recursion. But it involves choosing
     only option out of any possibilities. We begin by choosing an
     option and backtrack from it, if we reach a state where we conclude
     that this specific option does not give the required solution. We
     repeat these steps by going across each available option until we get
     the desired solution.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: utils/backtrack.py
     Created on 22 August, 2018 @ 8:57 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


def permute(idx, values):
    if idx == 1:
        return values

    return [y + x for y in permute(1, values)
            for x in permute(idx - 1, values)]


if __name__ == '__main__':
    print(permute(1, ["a", "b", "c"]))
    print(permute(2, ["a", "b", "c"]))
    # print(permute(3, ["a", "b", "c"]))
