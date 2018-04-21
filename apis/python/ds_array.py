"""Array is a container which can hold a fixed number of items and these items should be of the same type. Most of the data structures make use of arrays to implement their algorithms. Following are the important terms to understand the concept of Array:

    - Element: Each item stored in an array is called element.
    - Index: Each loacation of an element in an array has a numerical index, which is used to identify the element.

Basic Operations:

Following are the basic operations supported by an array.
    - Traverse: Print all the array elements one by one.
    - Insertion: Adds an element at the given index
    - Deletion: Deletes an element at the given index.
    - Search: Searches an element using the given index or by the value.
    - Update: Updates an element at the given index.

Syntax:

Array is created in Python by importing array module to the Python program. The array is declared as shown below:

    ```python
    >>> from array import *
    >>> arrayName = array(typecode, [Initializers])
    ```

Typecode are the codes that are used to define the type of value the array will hold. Some common typecodes used are:

    Typecode                        Value
        b           Represents signed integer of size 1 byte.
        B           Represents unsigned integer of size 1 byte.
        c           Represents character of size 1 byte.
        i           Represents signed integer of size 2 bytes.
        I           Represents unsigned integer of size 2 bytes.
        f           Represents floating point of size 4 bytes.
        d           Represents folating point of size 8 bytes.

Example:

In [1]
    ```python
    arr = array('i', [10, 20, 30, 40, 50])

    for x in arr:
        print(x)
    ```

Output:
    ```sh
    10
    20
    30
    40
    50

    ```
"""
