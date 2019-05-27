"""Matrix is a special case of two dimensional array where each data element
is of strictly same size. So every matrix is also a two dimensional array but
not vice versa. Matrices are very important data structures for many
mathematical and scientific calculations.

Numpy is a third-party C-optimized library which has extensive support for
scientific and mathematical calculations. NumPy has a relatively simple API
with lots of functionality widely adopted in the Python scientific community.

For simple matrix operations we we'll use NumPy. Visit <http://numpy.org> for
more info.

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

Matrix Example: Consider the case of reading temperature for 1 week measured
in the morning, mid-day, evening and mid-night. We can determine the shape of
the matrix by using the `.shape` attribute on the data object. In this case
since we have 5 columns of data and 7 days of the week, the shape is 7x5.

    ```python
    >>> import numpy as np
    >>> matrix = np.array([['Mon', 18, 20, 22, 17],
    ...                    ['Tue', 11, 18, 21, 18],
    ...                    ['Wed', 15, 21, 20, 19],
    ...                    ['Thu', 11, 20, 22, 21],
    ...                    ['Fri', 18, 17, 23, 22],
    ...                    ['Sat', 12, 22, 20, 18],
    ...                    ['Sun', 13, 15, 19, 16]])
    >>> matrix.shape
    (7, 5)
    ```
"""
# NumPy is a third party library which can be install using pip
# $ pip3 install scipy numpy
import numpy as np

# Temperature reading for 1 week.
data = np.array([['Mon', 18, 20, 22, 17],
                 ['Tue', 11, 18, 21, 18],
                 ['Wed', 15, 21, 20, 19],
                 ['Thu', 11, 20, 22, 21],
                 ['Fri', 18, 17, 23, 22],
                 ['Sat', 12, 22, 20, 18],
                 ['Sun', 13, 15, 19, 16]])

print('Matrix data:\n{}'.format(data))
print('data.shape = {}'.format(data.shape))

# Accessing values in a matrix.
print('\nAccessing values in a matrix:')
print('data[2] = {}'.format(data[2]))
print('data[4][3] = {}'.format(data[4][3]))

# Adding a row.
print('\nAdding a row:')
row = np.append(data, [['Avg', 12, 15, 13, 11]], axis=0)

print('\nAverage:\n{}'.format(row))
print('row.shape = {}'.format(row.shape))

# Adding a column.
print('\nAdding a column:')
col = np.insert(data, obj=[5],
                values=[[1], [2], [3], [4], [5], [6], [7]],
                axis=1)
print('col:\n{}'.format(col))

# Delete a row from a matrix.
print('\nDelete a row from a matrix:')
data = np.delete(data, obj=[2], axis=0)
print('data:\n{}'.format(data))

# Delete a column from a matrix.
print('\nDelete a column from a matrix:')
data = np.delete(data, obj=[2], axis=1)
print('data:\n{}'.format(data))

# Update a row in a matrix.
print('\nUpdate a row in a matrix:')
data[3] = ['Thu', 10, 10, 10]
print('data:\n{}'.format(data))

# Update a column in a matrix.
data[2][0] = 'Wed'
print('data:\n{}'.format(data))

# Access a single column.
print('\nAccess the days of the week:')
print('data[:,0] = {}'.format(data[:, 0]))

# Access multiple columns.
print('\nAccess all temperature data:')
print('\ndata[:,1:] =>\n{}'.format(data[:, 1:]))
