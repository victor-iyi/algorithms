"""List is the most versatile data type available in Python which can be written as a list of comma-separated values (items) between square brakets. Important thing about a list is that items in a list need not to be of the same type (Unlike numsays).

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

# Declaring a list.
data = ['Physics', 'Chemistry', 1997, 2000]
nums = [10, 20, 30, 40, 50]

print('\nDeclaring lists:')
print('data = {}'.format(data))
print('nums = {}'.format(nums))

print('\nAccessing elements of a list:')
print('data[0]  : {}'.format(data[0]))
print('nums[1:5]: {}'.format(nums[1:5]))

print('\nUpdating lists:')

print('Old value of data[2]: {}'.format(data[2]))

# Update the element in the 3rd index to 'Math'.
data[2] = 'Math'

print('New value of data[2]: {}'.format(data[2]))

# Insertion Operation.
print('\nInserting `60` at the 2nd index:')
nums.insert(1, 60)

for a in nums:
    print(a)

# Deletion operation.
print('\nRemove element `40` from the numsay.')
nums.remove(40)

for i, a in enumerate(nums):
    print('nums[{}] = {}'.format(i, a))


# Search operation.
print('\nSearch retruns the index an element is located:')
idx = nums.index(30)
print('{} is at index: {}'.format(30, idx))

# Update operation.
print('\nUpdate the element at index `2`:')

# Before update:
print('Before: nums[2] = {}'.format(nums[2]))
print(nums)

# Update element at the 3rd index.
nums[2] = 80

# After update:
print('After : nums[2] = {}'.format(nums[2]))
print(nums)
