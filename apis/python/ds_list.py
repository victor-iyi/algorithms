"""List is the most versatile data type available in Python which can be written as a list of comma-separated values (items) between square brakets. Important thing about a list is that items in a list need not to be of the same type (Unlike arrays).

Creating a list is as simple as putting different comma-separated values between square brakets. 
For example:

    ```python
    >>> list1 = ['Physics', 'Chemistry', 1997, 2000]
    >>> list2 = [1, 2, 3, 4, 5]
    >>> list3 = ['a', 'b', 'c', 'd']
    ```

Basic Operations:

List respond to the `+` and `*` operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

     Description            Python Expression                Results
        Length                  len([1, 2, 3])                  3                 
        Concatenation           [1, 2, 3] + [4, 5, 6]           [1, 2, 3, 4, 5, 6]
        Repetition              ['Hi'] * 3                      ['Hi', 'Hi', 'Hi']
        Membership              3 in [1, 2, 3]                  True              
        Iteration               for x in [1, 2, 3]:             1 2 3             
                                  print(x, end=' ')

"""
