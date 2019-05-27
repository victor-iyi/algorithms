"""Sort Algorithms: Merge Sort.

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: sort/merge.py
     Created on 22 August, 2018 @ 8:58 PM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted

    mid = len(unsorted) // 2

    left = merge_sort(unsorted[:mid])
    right = merge_sort(unsorted[mid:])

    return merge(left, right)


def merge(left, right):
    temp = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            temp.append(left[0])
            del left[0]
        else:
            temp.append(right[0])
            del right[0]

    # Cos it's a recursive solution:
    temp += right if len(left) == 0 else left

    return temp


if __name__ == '__main__':
    unsorted_int = [3, 2, 5, 52, 1, 5, 3, 2, 1, 2]
    sorted_int = merge_sort(unsorted_int)
    print('Unsorted: {}'.format(unsorted_int))
    print('Sorted:   {}'.format(sorted_int))

    print()

    unsorted_char = ['V', 'I', 'C', 'T', 'O', 'R']
    sorted_char = merge_sort(unsorted_char)
    print('Unsorted: {}'.format(unsorted_char))
    print('Sorted:   {}'.format(sorted_char))
