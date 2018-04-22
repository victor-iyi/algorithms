"""Matrix is a special case of two dimensional array where each data element is of strictly same size. So every matrix is also a two dimensional array but not vice versa. Matrices are very important data structures for many mathematical and scientific calculations.

Numpy is a third-party C-optimized library which has extensive support for scientific and mathematical calculations. NumPy has a relatively simple API with lots of functionalities widely adopted in the Python scientific community.

For simple matrix operations we we'll use NumPy. Visit http://numpy.org for more info.

Installation:
    ```sh
    pip3 install numpy scipy
    ```

Usage:
    ```python
    >>> import numpy as np
    >>> a = np.array([[1, 2, 3], [4, 5, 6]])
    >>> a.shape
    (2, 3)
    ```
Matrix Example:
    Consider the case of reading temprature for 1 week measured in the morning, mid-day, evening and mid-night. It can be presented as a 7x5 matrix using an array and the reshape method available in numpy.

    ```python
    >>> import numpy as np
    >>> a = np.array([['Mon', 18, 20, 22, 17],
                      ['Tue', 11, 18, 21, 18],
                      ['Wed', 15, 21, 20, 19],
                      ['Thu', 11, 20, 22, 21],
                      ['Fri', 18, 17, 23, 22],
                      ['Sat', 12, 22, 20, 18],
                      ['Sun', 13, 15, 19, 16]])
    >>> a.shape

    ```
"""
import numpy as np

a = np.array([['Mon', 18, 20, 22, 17],
              ['Tue', 11, 18, 21, 18],
              ['Wed', 15, 21, 20, 19],
              ['Thu', 11, 20, 22, 21],
              ['Fri', 18, 17, 23, 22],
              ['Sat', 12, 22, 20, 18],
              ['Sun', 13, 15, 19, 16]])

print('Matrix a:\n{}\n'.format(a))
print('a.shape = {}'.format(a.shape))
